from itertools import groupby
from twod import cross3
def convex_hull_graham_scan(points):
    def remove_duplicates(points):
        points.sort()
        return list(k for k, _ in groupby(points))
    def build_hull(points):
        hull = []
        for point in points:
            while len(hull) >= 2 and cross3(hull[-2], hull[-1], point) <= 0:
                hull.pop()
            hull.append(point)
        return hull
    points = remove_duplicates(points)
    if len(points) <= 1: return points
    points.sort()
    lower_hull = build_hull(points)
    upper_hull = build_hull(reversed(points))
    return lower_hull[:-1] + upper_hull[:-1]