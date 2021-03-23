# Create an unweighted, directed graph

class Graph:

  def __init__(self):
    self.graph = {}

  def add_node(self, node):
    if node in list(self.graph.keys()):
      raise KeyError("Node already in graph")
    self.graph[node] = {}

  def add_edge(self, node1, node2, weight=0):
    if node1 not in list(self.graph.keys()):
      self.add_node(node1)
    if node2 not in list(self.graph.keys()):
      self.add_node(node2)
    if node2 not in list(self.graph[node1].keys()):
      self.graph[node1][node2] = weight

  def nodes(self):
    node_list = []
    for node in list(self.graph.keys()):
      node_list.append(node)
    return node_list
  
  def edges(self):
    edge_list = []
    for node in list(self.graph.keys()):
      edge_list.append("{}: {}".format(node, list(self.graph[node].keys())))
    return edge_list

dummy = Graph()
dummy.add_edge(1, 2, 2)
dummy.add_edge(1, 3, 1)
dummy.add_edge(2, 4, 4)
dummy.add_edge(3, 5, 3)
dummy.add_edge(4, 6, 6)
dummy.add_edge(5, 6, 5)
dummy.add_edge(7, 4)

print(dummy.nodes())
print(dummy.edges())