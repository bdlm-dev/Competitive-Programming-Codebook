def shortest_path(digr, s):
    """ Finds the shortest path from s to every other vertex findable
    from s using Dijkstra's algorithm in O(mlogn) time"""
    nodes_explored = set([s])
    nodes_unexplored = DFS(digr, s) # all accessible nodes from s
    nodes_unexplored.remove(s)
    dist = {s:0}
    node_heap = []
    for n in nodes_unexplored:
        min = compute_min_dist(digr, n, nodes_explored, dist)
        heapq.heappush(node_heap, (min, n))
    while len(node_heap) > 0:
        min_dist, nearest_node = heapq.heappop(node_heap)
        dist[nearest_node] = min_dist
        nodes_explored.add(nearest_node)
        nodes_unexplored.remove(nearest_node)
        for v in digr.neighbors(nearest_node):
            if v in nodes_unexplored:
                for i in range(len(node_heap)):
                    if node_heap[i][1] == v:
                        node_heap[i] = (compute_min_dist(digr, v, nodes_explored, dist), v)
                        heapq.heapify(node_heap)
    return dist
def compute_min_dist(digr, n, nodes_explored, dist):
    """ Computes the min dist of node n from a set of
    nodes explored in digr, using dist dict. Used in shortest path """
    min = float('inf')
    for v in nodes_explored:
        if digr.has_edge((v, n)):
            d = dist[v] + digr.get_edge_weight((v, n))
            if d < min: min = d
    return min