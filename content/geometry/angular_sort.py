from math import atan2
# Sort list of points (x, y) counter-clockwise in-place
def angular_sort(p):
    p.sort(key=lambda point: (atan2(point[1], point[0]), -point[0], -point[1]))