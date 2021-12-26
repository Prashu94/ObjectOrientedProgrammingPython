import math

# Example of calculating the distance between points without object oriented programming.
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def perimeter(polygon):
    perimeter = 0
    points = polygon + [polygon[0]]
    print(points)
    for i in range(len(polygon)):
        perimeter += distance(points[i] , points[i+1])
    return perimeter


# Created the class Point to collect the points, instead of storing in list as done earlier.
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, p2):
        return math.sqrt((self.x-p2.x)**2 + (self.y - p2.y)**2)


class Polygon:
    # Store the Points object in the Polygon object
    def __init__(self):
        self.vertices = []

    def add_point(self, point):
        self.vertices.append((point))

    def perimeter(self):
        perimeter = 0
        points = self.vertices + [self.vertices[0]]
        for i in range(len(self.vertices)):
            perimeter += points[i].distance(points[i+1])
        return perimeter


if __name__=='__main__':

    #square = [(1,1),(1,2),(2,2),(2,1)]
    #print(perimeter(square))

    square = Polygon()
    square.add_point(Point(1, 1))
    square.add_point(Point(1, 2))
    square.add_point(Point(2, 2))
    square.add_point(Point(2, 1))

    print(square.perimeter())



