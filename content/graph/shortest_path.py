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

def alt_dijkstra_algorithm(graph, start_node):
    unvisited_nodes = list(graph.nodes())
    # We'll use this dict to save the cost of visiting each node and update it as we move along the graph
    shortest_path = {}
    # We'll use this dict to save the shortest known path to a node found so far
    previous_nodes = {}
    # We'll use max_value to initialize the "infinity" value of the unvisited nodes
    max_value = float('inf')
    for node in unvisited_nodes:
        shortest_path[node] = max_value
    # However, we initialize the starting node's value with 0
    shortest_path[start_node] = 0
    # The algorithm executes until we visit all nodes
    while unvisited_nodes:
        # The code block below finds the node with the lowest score
        current_min_node = None
        for node in unvisited_nodes:  # Iterate over the nodes
            if current_min_node is None:
                current_min_node = node
            elif shortest_path[node] < shortest_path[current_min_node]:
                current_min_node = node
        # The code block below retrieves the current node's neighbors and updates their distances
        neighbors = graph.neighbors(current_min_node)
        for neighbor in neighbors:
            tentative_value = shortest_path[current_min_node] + graph.get_edge_weight((current_min_node, neighbor))
            if tentative_value < shortest_path[neighbor]:
                shortest_path[neighbor] = tentative_value
                # We also update the best path to the current node
                previous_nodes[neighbor] = current_min_node
        # After visiting its neighbors, we mark the node as "visited"
        unvisited_nodes.remove(current_min_node)
    return previous_nodes, shortest_path