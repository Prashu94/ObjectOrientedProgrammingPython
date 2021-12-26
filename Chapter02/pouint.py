# Create a class Point
import math


class Point:
    '''
    Note: self argument to the method is simply the reference to the object
    that the method is being invoked on.
    '''
    # add the attributes to the class
    def __init__(self, x=0, y=0):
        self.move(x,y)

    # Method to be called from the constructor to set the attributes x and y
    def move(self,x,y):
        self.x = x
        self.y = y

    # Method to reset the x and y attributes of the class
    def reset(self):
        self.move(0,0)

    # Method to calculate the distance between 2 points
    def calculate_distance(self, other_point):
        return math.sqrt((self.x - other_point.x)**2
                         + (self.y - other_point.y)**2)

# Initialize 2 objects
#point1=Point()
#point2=Point()

# Add attributes to these objects
#point1.x = 4
#point1.y = 5

#point2.x = 6
#point2.y = 7

#print(point1.x, point2.x)
#print(point1.y, point2.y)

# Initialize the points through constructors
# point1 = Point(1,4)
# point2 = Point(2,5)
# print(point1.x, point2.x)
# print(point1.y, point2.y)

# Initialize the object
point1 = Point()
point2 = Point()

# Reset the values of point1
point1.reset()
# Move the point2 to a specific place
point2.move(5,0)
# Calculate the distance between point1 and point2
print(point2.calculate_distance(point1))

# Test the symmetrical attribute
assert point2.calculate_distance(point1) == point1.calculate_distance(point2)

# Move the point1 to 3,4
point1.move(3,4)
print(point1.calculate_distance(point2))
print(point2.calculate_distance(point1))