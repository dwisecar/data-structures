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
  
  def delete_node(self, node):
    if node not in list(self.graph.keys()):
      raise KeyError("Node not in graph")
    del self.graph[node]
    for key in list(self.graph.keys()):
      if key in list(self.graph[key].keys()):
        del self.graph[key][node]

  def delete_edge(self, node1, node2):
    if node2 in list(self.graph[node1].keys()) and self.graph[node2]:
      del self.graph[node1][node2]
    elif node1 not in list(self.graph.keys()) or node2 not in list(self.graph.keys()):
      raise KeyError("Node not in graph")
    else:
      raise ValueError("No edge for these nodes")

  def has_node(self, node):
    return node in list(self.graph.keys())

  def neighbors(self, node):
    if node not in list(self.graph.keys()):
      raise KeyError("Node Not in here")
    return self.graph[node]

  def adjacent(self, node1, node2):
    # return true if they are connected by an edge
    if node1 not in list(self.graph.keys()):
      raise KeyError("{} not in graph".format(node1))
    if node2 not in list(self.graph.keys()):
      raise KeyError("{} not in graph".format(node2))
    return node1 in list(self.graph[node2].keys()) or node2 in list(self.graph[node1].keys())

  def depth_traversal(self, start, checked=None):
    if start not in list(self.graph.keys()):
      raise KeyError("{} not in graph.".format(start))
    if checked is None:
      checked = []
    checked.extend([start])
    for edge in list(self.graph[start].keys()):
      if edge not in checked:
        self.depth_traversal(edge, checked)
    return checked



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
dummy.delete_node(7)
print(dummy.nodes())
print(dummy.edges())