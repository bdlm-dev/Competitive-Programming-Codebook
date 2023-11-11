def DFS(gr, s):
    """ Depth first search wrapper """
    path = set([])
    depth_first_search(gr, s, path)
    return path
def depth_first_search(gr, s, path):
    """ Depth first search
    Returns a list of nodes "findable" from s """
    if s in path: return False
    path.add(s)
    for each in gr.neighbors(s):
        if each not in path:
            depth_first_search(gr, each, path)