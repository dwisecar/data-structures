class Node
  attr_accessor :next
  attr_reader :value
  def initialize(value)
    @value = value
    @next = nil
  end

end

class LinkedList
  def initialize
    @head = nil
  end

  def find_end
    node = @head
    return node if !node.next
    return node if !node.next while (node = node.next)
  end

  def find(value)
    node = @head
    return false if !node.next
    return node if node.value == value

    while (node = node.next)
      return node if node.value == value
    end
  end

  def append(value)
    new_node = Node.new(value)
    if @head
      find_end.next = new_node
    else
      @head = new_node
    end
  end

  def append_after(target, value)
    new_node = Node.new(value)
    node = find(target)
    if node
      new_node.next = node.next
      node.next = new_node
    end 
  end

  def delete(value)
    node = @head
    if node.value == value
      @head = @head.next
      return
    end
    while node.next
      if node.next.value == value
        break
      end
      node = node.next
    end
    if node
      node.next = node.next.next
    else
      p "Value not found"
    end
  end

  def print_list
    node = @head
    while node
      p node.value
      node = node.next
    end
  end

end

ll = LinkedList.new

ll.append("Monday")
ll.append("Wednesday")
ll.append("Thursday")
ll.append("Friday")
ll.append("Saturday")
ll.print_list
ll.append_after("Monday", "Tuesday")
ll.delete("Friday")
ll.print_list
