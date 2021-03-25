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
      if node in list(self.graph[key].keys()):
        del self.graph[key][node]

  def delete_edge(self, node1, node2):
    if node2 in list(self.graph[node1].keys()) and self.graph[node2]:
      del self.graph[node1][node2]
    elif node1 not in list(self.graph.keys()) or node2 not in list(self.graph.keys()):
      raise KeyError("Node not in graph")
    else:
      raise ValueError("No edge for these nodes")

  def delete_edge(self, n1, n2):
    if n2 in list(self.graph[n1].keys()) and self.graph[n2]:
      del self.graph[n1][n2]
    elif n1 not in list(self.graph.keys()) or n2 not in list(self.graph.keys()):
      raise KeyError("Node not here")
    else:
      raise KeyError("No edge")

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

  def depth_traversal(self, start, visited=None):
    if start not in list(self.graph.keys()):
      raise KeyError("{} not in graph.".format(start))
    if visited is None:
      visited = []
    visited.extend([start])
    for edge in list(self.graph[start].keys()):
      if edge not in visited:
        self.depth_traversal(edge, visited)
    return visited

  def breath_traversal(self, start):
    visited, node_list = [], [start]
    while node_list:
      vertex = node_list.pop(0)
      if vertex not in visited:
        visited.append(vertex)
        [node_list.append(edge) for edge in list(self.graph[vertex].keys()) 
          if edge not in visited]
    return visited

  def dijkstra(self, start, finish):
        """Return the shortest path between two nodes.
        Return the path and the number of steps taken to follow that path."""

        unvisited = self.depth_traversal(start)
        distances = {i: [None, [None]] for i in unvisited}
        distances[start] = [0, [start]]
        current_node = start

        if start not in unvisited:
            raise KeyError("The start node is not in the graph.")
        elif finish not in unvisited:
            raise ValueError("The finish node is not in the graph.")

        while unvisited:
            for item in self.neighbors(current_node):
                study_node = item
                current_node_distance = distances[current_node][0]
                potential_distance = self.neighbors(current_node)[study_node]
                original_distance = distances[study_node][0]

                if study_node not in unvisited:
                    continue
                elif original_distance is None or potential_distance < original_distance:
                    current_node_path = (distances[current_node])[1][:]
                    current_node_path.append(study_node)
                    distances[study_node][0] = potential_distance + current_node_distance
                    distances[study_node][1] = current_node_path
                    continue

            if current_node == finish:
                return distances[finish]

            unvisited.remove(current_node)
            next_node = None
            for key, value in distances.items():
                if key in unvisited:
                    if next_node is None:
                        next_node = key
                        continue
                    elif distances[key][0]:
                        if distances[key][0] < distances[next_node][0]:
                            next_node = key
            current_node = next_node

dummy = Graph()
dummy.add_edge(1, 2, 2)
dummy.add_edge(1, 3, 1)
dummy.add_edge(2, 4, 4)
dummy.add_edge(3, 5, 3)
dummy.add_edge(4, 6, 6)
dummy.add_edge(5, 6, 5)
dummy.add_edge(7, 4, 1)


# print(dummy.nodes())
# print(dummy.edges())
# dummy.delete_node(7)
# print(dummy.nodes())
# print(dummy.edges())
# print(dummy.adjacent(1,7))
print(dummy.depth_traversal(4))
print(dummy.breath_traversal(4))
print(dummy.dijkstra(1,6))
