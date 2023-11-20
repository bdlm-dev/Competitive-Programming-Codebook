# Get area of polygon from list of vertices
def get_area(verts):
    area = 0
    n = len(verts)
    for i in range(n-1):
        j = i+1 % n
        area += verts[i][0] * verts[j][1]
        area -= verts[i][1] * verts[j][0]
    return abs(area/2)