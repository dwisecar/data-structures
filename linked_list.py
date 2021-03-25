class Node:
  def __init__(self, data):
    self.next = None
    self.data = data

class LinkedList:
  def __init__(self):
    self.head = None

  def get_count(self):
    count = 0
    temp = self.head
    while temp is not None:
      count +=1
      temp = temp.next
    return count

  def list_print(self):
    temp = self.head
    while temp is not None:
      print(temp.data)
      temp = temp.next

  def append(self, data):
    node = Node(data)
    if self.head is None:
      self.head = node
      return
    temp = self.head
    while temp.next:
      temp = temp.next
    temp.next = node

  def push(self, data):
    node = Node(data)
    node.next = self.head
    self.head = node

  def add_node_to_middle(self, node, data):
    new_node = Node(data)
    new_node.next = node.next
    node.next = new_node

  def delete_data(self, data):
    temp = self.head
    prev = None
    while temp is not None:
      if temp.data == data:
        break
      else:
        prev = temp
        temp = temp.next
    if prev is None:
      self.head = temp.next
    elif prev and temp:
      prev.next = temp.next
    else:
      raise ValueError("No node with {} as data".format(data))



list1 = LinkedList()
list1.head = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")
e4 = Node("Thur")
#link the first node to the second node
list1.head.next = e2
#link the rest in order
e2.next = e3
e3.next = e4
list1.push("Sun")
list1.append("Saturday baby wooo")
list1.add_node_to_middle(e4, "Fri")
list1.delete_data("Tue")
list1.list_print()
print(list1.get_count())