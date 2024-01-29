import cv2
import numpy as np

# Görüntüyü yükle
image_path = "/Users/ufukdemirtas/Desktop/final_Goruntu/OutPuts/Output5.png"
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(image, connectivity=8)
for label in range(1, num_labels):
    area = stats[label, cv2.CC_STAT_AREA]
    left_top_x = stats[label, cv2.CC_STAT_LEFT]
    left_top_y = stats[label, cv2.CC_STAT_TOP]
    width = stats[label, cv2.CC_STAT_WIDTH]
    height = stats[label, cv2.CC_STAT_HEIGHT]

    moments = cv2.moments((labels == label).astype(np.uint8))

    # Yön
    orientation = 0.5 * np.arctan2(2 * moments['mu11'], moments['mu20'] - moments['mu02'])

    # Dairesellik
    circularity = (4 * np.pi * area) / (width ** 2)

    # Sonuç
    print(f"Bölge {label}:")
    print(f" - alan: {area}")
    print(f" - yön: {orientation}")
    print(f" - Dairesellik: {circularity}")

    cv2.rectangle(image, (left_top_x, left_top_y), (left_top_x + width, left_top_y + height), (255, 255, 255), 2)

# Sonuçları göster
cv2.imshow("Labeled Components", image)
cv2.waitKey(0)
cv2.destroyAllWindows()