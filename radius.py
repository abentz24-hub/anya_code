#area_circle.py

def circle_area(radius):
    area = 3.1415 * radius ** 2
    return area


def rectangle_area(length,width):
    area = length * width
    return area
    
print(circle_area(2))
print("The area of the rectangle is",rectangle_area,(5,8))