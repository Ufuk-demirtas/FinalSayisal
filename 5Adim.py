import cv2
import numpy as np
import os

image_path = "/Users/ufukdemirtas/Desktop/final_Goruntu/OutPuts/Output4.png"
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Bileşen Etiketleme
num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(image, connectivity=8)
colors = np.random.randint(0, 255, size=(num_labels, 3), dtype=np.uint8)
colored_labels = np.zeros((image.shape[0], image.shape[1], 3), dtype=np.uint8)

# Renklendir
for label in range(3, num_labels):
    colored_labels[labels == label] = colors[label]

# Kaydet
desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
cv2.imwrite(os.path.join(desktop_path, 'Output5.png'), colored_labels)
cv2.imshow("Original Image", image)
cv2.imshow("Colored Labels", colored_labels)
cv2.waitKey(0)
cv2.destroyAllWindows()