import pydicom
import cv2
import numpy as np
import matplotlib.pyplot as plt
from pydicom.pixel_data_handlers.util import apply_modality_lut, apply_voi_lut

file_name = '0002.DCM'
dcm = pydicom.dcmread(file_name)
#print(dcm)

images = dcm.pixel_array
print(type(images))
print(images.shape)

#rescale slope/intercept 값 가져오기 (default: 1, 0)
rescale_slope = dcm.get("RescaleSlope", 1)
rescale_intercept = dcm.get("RescaleIntercept", 0)

image = rescale_slope * images[0] + rescale_intercept

plt.subplot(1,3,1)
plt.title("original dicom file")
plt.imshow(image, cmap = 'gray')


# pydicom module로 window level 설정하기

window_center = 700
window_width = 1400

dcm.WindowCenter = window_center
dcm.WindowWidth = window_width

modality_lut_image = apply_modality_lut(image, dcm)
voi_lut_image = apply_voi_lut(modality_lut_image, dcm)

plt.subplot(1,3,2)
plt.title('apply_voi_lut')
plt.imshow(voi_lut_image, cmap = 'gray')
plt.axis('off')

# 직접 windowing 설정하여 normalization 해보기
# 초기 WW / WL 설정

window_image = np.clip(image, window_center - (window_width / 2), window_center + (window_width / 2))

plt.subplot(1,3,3)
plt.title('windowing')
plt.imshow(window_image, cmap = 'gray')
plt.axis('off')
plt.show()
