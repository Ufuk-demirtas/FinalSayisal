import cv2
import numpy as np
import os

image_path = "/Users/ufukdemirtas/Desktop/final_Goruntu/OutPuts/OutPut2.png"
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
# Eşikleme
_, thresholded = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY)
# filtreleme
min_component_size = 1000
filtered_image = np.zeros_like(thresholded)
_, labels, stats, _ = cv2.connectedComponentsWithStats(thresholded, connectivity=8)
for label in range(1, len(stats)):
    if stats[label, cv2.CC_STAT_AREA] >= min_component_size:
        filtered_image[labels == label] = 255

kernel = np.ones((2, 2), np.uint8)
eroded_image = cv2.erode(filtered_image, kernel, iterations=1)

# Kaydet
desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
cv2.imwrite(os.path.join(desktop_path, 'filtered_3_1.jpg'), eroded_image)
edges = cv2.Canny(eroded_image, 100, 200)

# Kaydet
cv2.imwrite(os.path.join(desktop_path, 'edges_3_2.jpg'), edges)

# Sonuçlar
cv2.imshow('Original Resim', image)
cv2.imshow('Filtered and Eroded Resim', eroded_image)
#cv2.imshow('Edges Image', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
