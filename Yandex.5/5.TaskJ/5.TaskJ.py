import matplotlib.pyplot as plt

points = []
x_coord = []
y_coord = []
numofpoints = int(input())
for i in range(numofpoints):
    maininput = input()
    x, y = list(map(int, maininput.split()))
    points.append((x, y))
    x_coord.append(x)
    y_coord.append(y)

def count_isosceles_triangles():
    n = len(points)
    total_triangles = set()
    
    for i in range(n):
        distances = {}
        for j in range(n):
            if i != j:
                dist_squared = (x_coord[i] - x_coord[j])**2 + (y_coord[i] - y_coord[j])**2
                if dist_squared in distances:
                    distances[dist_squared].append(j)
                else:
                    distances[dist_squared] = [j]
        
        for coord in distances.values():
            if len(coord) > 1:
                for j in range(len(coord)):
                    for k in range(j + 1, len(coord)):
                        triangle = tuple(sorted([i, coord[j], coord[k]]))
                        total_triangles.add(triangle)
    
    return len(total_triangles)

print(count_isosceles_triangles())




