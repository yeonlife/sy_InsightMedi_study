import os
import glob
import sys
import cv2
import pydicom
import numpy as np
from PyQt5.QtCore import QDir, Qt
from PyQt5.QtGui import QImage, QPainter, QPalette, QPixmap, qRgb
from PyQt5.QtWidgets import (QAction, QApplication, QFileDialog, QLabel,
        QMainWindow, QMenu, QMessageBox, QScrollArea, QSizePolicy, QInputDialog)
from PyQt5.QtPrintSupport import QPrintDialog, QPrinter

class ImageViewer(QMainWindow):
    def __init__(self):
        super(ImageViewer, self).__init__()
        self.gray_color_table = [qRgb(i, i, i) for i in range(256)]
        #self.base_path = './image_path'
        #self.img_list = glob.glob(os.path.join(self.base_path, '*.jpg'))
        self.dcm = pydicom.read_file('0002.DCM')
        self.dcm_images = self.dcm.pixel_array
        self.pos = 0
        self.image_array = np.array(self.dcm_images[self.pos], dtype=np.uint8)
        self.total = self.dcm_images.shape[0]

        self.printer = QPrinter()
        self.width = 620
        self.height = 620       
        self.imageLabel = QLabel()
        self.imageLabel.setBackgroundRole(QPalette.Base)
        self.imageLabel.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.imageLabel.setScaledContents(True)

        self.scrollArea = QScrollArea()
        self.scrollArea.setBackgroundRole(QPalette.Dark)
        self.scrollArea.setWidget(self.imageLabel)
        self.setCentralWidget(self.scrollArea)
        self.createActions()

        self.setWindowTitle("Image Viewer")
        self.resize(self.width, self.height)

        #image = cv2.imshow('Grayscale Image', self.image_array)
        self.openImage(image=self.toQImage(self.image_array))
    
    def normalSize(self):
        self.imageLabel.adjustSize()

    def fitToWindow(self):
        fitToWindow = self.fitToWindowAct.isChecked()
        self.scrollArea.setWidgetResizable(fitToWindow)
        if not fitToWindow:
            self.normalSize()
        self.updateActions()
        
    def createActions(self):
        self.normalSizeAct = QAction("&Normal Size", self, shortcut="Ctrl+S",
                enabled=False, triggered=self.normalSize)
        self.fitToWindowAct = QAction("&Fit to Window", self, enabled=False,
                checkable=True, shortcut="Ctrl+F", triggered=self.fitToWindow)
        
    def updateActions(self):
        self.normalSizeAct.setEnabled(not self.fitToWindowAct.isChecked())
       
    def adjustScrollBar(self, scrollBar, factor):
        scrollBar.setValue(int(factor * scrollBar.value()
                                + ((factor - 1) * scrollBar.pageStep()/2)))
    
    def toQImage(self, im, copy=False):
        if im is None:
            return QImage()
        
        if im.dtype == np.uint8:
            if len(im.shape) == 2:
                qim = QImage(im.data, im.shape[1], im.shape[0], im.strides[0], QImage.Format_Indexed8)
                qim.setColorTable(self.gray_color_table)
                return qim.copy() if copy else qim
        elif len(im.shape) == 3:
            if im.shape[2] == 3:
                qim = QImage(im.data, im.shape[1], im.shape[0], im.strides[0], QImage.Format_RGB888)
                return qim.copy() if copy else qim
            elif im.shape[2] == 4:
                qim = QImage(im.data, im.shape[1], im.shape[0], im.strides[0], QImage.Format_ARGB32)
                return qim.copy() if copy else qim
    
    def openImage(self, image=None, fileName=None):
        if image == None:
            image = QImage(fileName)
        if image.isNull():
            QMessageBox.information(self, "Image Viewer",
                                    "Cannot load %s." % fileName)
            return
        
        self.imageLabel.setPixmap(QPixmap.fromImage(image))

        self.fitToWindowAct.setEnabled(True)
        self.updateActions()
        if not self.fitToWindowAct.isChecked():
            self.imageLabel.adjustSize()
        

    def keyPressEvent(self, e):
        if e.key() == 65:
            if not self.pos == 0:
                self.pos -= 1
                image = cv2.imread(self.img_list[self.pos])
                """
                이미지 처리
                """
                self.openImage(image=self.toQImage(image))
                print('\r' + self.img_list[self.pos], end="")
                                                
        elif e.key() == 68:
            self.pos += 1
            if self.total == self.pos:
                self.pos -= 1
            image = cv2.imread(self.img_list[self.pos])
            """
            이미지 처리
            """
            self.openImage(image=self.toQImage(image))            
            print('\r' + self.img_list[self.pos], end="")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ImageViewer()
    sys.exit(app.exec_())
