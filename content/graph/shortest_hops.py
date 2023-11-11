def shortest_hops(gr, s):
    """ Finds shortest number of hops to reach a node from s.
     Returns a dict mapping: destination node from s -> no. of hops
    """
    if not gr.has_node(s):
        raise Exception("Node %s is not in graph" % s)
    else:
        dist = {}
        q = deque([s])
        nodes_explored = set([s])
        for n in gr.nodes():
            if n == s: dist[n] = 0
            else: dist[n] = float('inf')
        while len(q) != 0:
            node = q.popleft()
            for each in gr.neighbors(node):
                if each not in nodes_explored:
                    nodes_explored.add(each)
                    q.append(each)
                    dist[each] = dist[node] + 1
        return dist