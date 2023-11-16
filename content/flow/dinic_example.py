# Read input
from content.flow.dinic import Dinic

dinic = Dinic()

# Read input
N, M = map(int, input().split())  # Assuming you receive N and M from input

# Add edges to the graph
for _ in range(M):
    u, v, c = map(int, input().split())  # Assuming edge information is read from input
    dinic.make_edge(u, v, c)

# Calculate maximum flow from node 1 (factory) to other nodes (warehouses)
max_flow = dinic.max_flow(1, N)  # Assuming the factory is always Node 1
print("Maximum flow from the factory to warehouses:", max_flow)