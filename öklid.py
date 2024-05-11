

# 2D uzaydaki noktaları temsil eden demet
points = [(10, 30), (20, 55), (32, 64), (14, 73),(99,150)]

# İki nokta arasındaki Öklidi hesaplayan fonksiyon 
def euclideanDistance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

# Nokta çiftleri arasındaki mesafeyi hesapla ve distances listesine ekleyin
distances = []
for i in range(len(points)):
    for j in range(i+1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# Min mesafe
min_distance = min(distances)
print("Minimum distance:", min_distance)
