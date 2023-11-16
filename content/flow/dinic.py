from collections import deque

class Dinic:
    class Edge:
        def __init__(self, to, cap, flow, rev):
            self.to = to
            self.cap = cap
            self.flow = flow
            self.rev = rev

    MAXN = 1000
    MAXF = 10**9

    def __init__(self):
        self.v = [[] for _ in range(self.MAXN)]
        self.top = [0] * self.MAXN
        self.deep = [0] * self.MAXN
        self.side = [0] * self.MAXN
        self.s = 0
        self.t = 0

    def make_edge(self, s, t, cap):
        self.v[s].append(self.Edge(t, cap, 0, len(self.v[t])))
        self.v[t].append(self.Edge(s, 0, 0, len(self.v[s]) - 1))

    def dfs(self, a, flow):
        if a == self.t or not flow:
            return flow
        while self.top[a] < len(self.v[a]):
            e = self.v[a][self.top[a]]
            if self.deep[a] + 1 == self.deep[e.to] and e.cap - e.flow:
                x = self.dfs(e.to, min(e.cap - e.flow, flow))
                if x:
                    e.flow += x
                    self.v[e.to][e.rev].flow -= x
                    return x
            self.top[a] += 1
        self.deep[a] = -1
        return 0

    def bfs(self):
        q = deque()
        self.deep = [0] * self.MAXN
        q.append(self.s)
        self.deep[self.s] = 1
        while q:
            tmp = q.popleft()
            for e in self.v[tmp]:
                if not self.deep[e.to] and e.cap != e.flow:
                    self.deep[e.to] = self.deep[tmp] + 1
                    q.append(e.to)
        return bool(self.deep[self.t])

    def max_flow(self, _s, _t):
        self.s = _s
        self.t = _t
        flow = 0
        while self.bfs():
            self.top = [0] * self.MAXN
            while True:
                tflow = self.dfs(self.s, self.MAXF)
                if not tflow:
                    break
                flow += tflow
        return flow

    def reset(self):
        self.side = [0] * self.MAXN
        self.v = [[] for _ in range(self.MAXN)]