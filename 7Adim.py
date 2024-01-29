import cv2
import numpy as np

image_path = "/Users/ufukdemirtas/Desktop/final_Goruntu/OutPuts/Output5.png"
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(image, connectivity=8)
contours, _ = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
for label in range(1, num_labels):
    area = stats[label, cv2.CC_STAT_AREA]  # Bölge alanı
    perimeter = cv2.arcLength(contours[label - 1], True)  # Bölge çevresi

    # Alanın çevreye oranını hesapla
    area_perimeter_ratio = area / perimeter

    # Kompaktlığı hesapla
    compactness = (4 * np.pi * area) / (perimeter ** 2)

    # Sonuçları yazdır
    print(f"Bölge {label}:")
    print(f" - Oranı: {area_perimeter_ratio}")
    print(f" - Kompaktlık: {compactness}")
image_colored = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

cv2.drawContours(image_colored, contours, -1, (0, 255, 0), 1)

# Sonuçları göster
cv2.imshow("Labeled Components with Contours", image_colored)
cv2.waitKey(0)
cv2.destroyAllWindows()