def kruskal_MST(gr):
    """ computes minimum cost spanning tree in undirected,
    connected graph using Kruskal's MST. Uses union-find data structure
    for running times of O(mlogn) """
    sorted_edges = sorted(gr.get_edge_weights())
    uf = UnionFind() # requires UnionFind
    min_cost = 0
    for (w, (u, v)) in sorted_edges:
        if (not uf.get_leader(u) and not uf.get_leader(v)) \
                or (uf.get_leader(u) != uf.get_leader(v)):
            uf.insert(u, v)
            min_cost += w
    return min_cost