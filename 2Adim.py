import cv2 as cv
from matplotlib import pyplot as plt
import os
# Görüntünün dosya yolunu belirtin
path = "/Users/ufukdemirtas/Desktop/final_Goruntu/OutPuts/OutPut1.png"
resim = cv.imread(path, 0)
resim = cv.medianBlur(resim, 5)
# Adaptive Gaussian Thresholding
th3 = cv.adaptiveThreshold(resim, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, \
                            cv.THRESH_BINARY, 9, 13)
th3 = th3[5:-5, 5:-5]
# Kaydet
desktop_path = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
cv.imwrite(os.path.join(desktop_path, 'OutPut2.png'), th3)
# Resmi göster
plt.imshow(th3, 'gray')
plt.title('Thresholding')
plt.xticks([]), plt.yticks([])
plt.show()
