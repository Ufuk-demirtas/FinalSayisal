import cv2
import numpy as np
import os

# Görüntüyü yükle
image_path = "/Users/ufukdemirtas/Desktop/final_Goruntu/OutPuts/edges_3_2.jpg"
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Etiketleme
num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(image, connectivity=8)
kernel = np.ones((10, 10), np.uint8)

dilated_labels = cv2.dilate(image, kernel, iterations=1)

# Sonuçları masaüstüne kaydet
desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
cv2.imwrite(os.path.join(desktop_path, 'Output4.png'), dilated_labels)

cv2.imshow("Original", image)
cv2.imshow("Dilated_Labels", dilated_labels)
cv2.waitKey(0)
cv2.destroyAllWindows()