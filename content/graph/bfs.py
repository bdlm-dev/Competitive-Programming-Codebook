from collections import deque
def BFS(gr, s):
    """ Breadth first search
    Returns list of nodes that are "findable" from s """
    if not gr.has_node(s):
        raise Exception("Node %s not in graph" % s)
    nodes_explored = {s}
    q = deque([s])
    while len(q)!=0:
        node = q.popleft()
        for each in gr.neighbors(node):
            if each not in nodes_explored:
                nodes_explored.add(each)
                q.append(each)
    return nodes_explored