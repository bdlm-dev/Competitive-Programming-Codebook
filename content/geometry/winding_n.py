from twod import cross3
# winding number method to determine whether given point is inside convex polygon
def winding_number(convex_polygon, point):
    wn = 0  # Initialize winding number
    n = len(convex_polygon)
    for i in range(n):
        x1, y1 = convex_polygon[i]
        x2, y2 = convex_polygon[(i + 1) % n]
        if y1 <= point[1]:  # Starting y-coordinate of the edge
            if y2 > point[1]:  # Ending y-coordinate of the edge
                if cross3((x1, y1), (x2, y2), point) > 0:
                    wn += 1
        else:
            if y2 <= point[1]:
                if cross3((x1, y1), (x2, y2), point) < 0:
                    wn -= 1
    return wn != 0  # If wn is not zero, the point is inside the polygon