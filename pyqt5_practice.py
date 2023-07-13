## Ex 6-4. QFileDialog.
import pydicom
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QFileDialog, QAction
from PyQt5.QtGui import QIcon
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt

class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.setLayout(self.layout)
        self.setGeometry(200,200,800,400)

    def initUI(self):
        self.fig = plt.Figure()
        self.canvas = FigureCanvas(self.fig)
        #self.setCentralWidget(self.canvas)

        openFile = QAction(QIcon('open.png'), 'Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open New File')
        openFile.triggered.connect(self.showDialog)

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile)

        #self.setWindowTitle('File Dialog')
        self.setGeometry(300, 300, 300, 200)
        self.show()

        # btn layout
        
        btnLayout = QVBoxLayout()
        btnLayout.addWidget(self.canvas)

        # canvasLayout
        canvasLayout = QVBoxLayout()

        self.layout = QHBoxLayout()
        self.layout.addLayout(btnLayout)
        self.layout.addLayout(canvasLayout)

    def showDialog(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', './')

        print(fname[0])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
