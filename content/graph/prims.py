def minimum_spanning_tree(gr):
    """ Uses prim's algorithm to return the minimum
    cost spanning tree in a undirected connected graph.
    Works only with undirected and connected graphs """
    s = list(gr.nodes()[0])
    nodes_explored = set([s])
    nodes_unexplored = gr.nodes()
    nodes_unexplored.remove(s)
    min_cost, node_heap = 0, []
    for n in nodes_unexplored:
        min = compute_key(gr, n, nodes_explored)
        heapq.heappush(node_heap, (min, n))
    while len(nodes_unexplored) > 0:
        node_cost, min_node = heapq.heappop(node_heap)
        min_cost += node_cost
        nodes_explored.add(min_node)
        nodes_unexplored.remove(min_node)
        for v in gr.neighbors(min_node):
            if v in nodes_unexplored:
                for i in range(len(node_heap)):
                    if node_heap[i][1] == v:
                        node_heap[i] = (compute_key(gr, v, nodes_explored), v)
                        heapq.heapify(node_heap)
    return min_cost
def compute_key(gr, n, nodes_explored):
    """ computes minimum key for node n from a set of nodes_explored
    in graph gr. Used in Prim's implementation """
    min = float('inf')
    for v in gr.neighbors(n):
        if v in nodes_explored:
            w = gr.get_edge_weight((n, v))
            if w < min: min = w
    return min