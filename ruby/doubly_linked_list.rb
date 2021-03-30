class DLLNode 
  attr_accessor :value, :prev, :next
  def initialize(value)
    @value = value
    @prev = nil
    @next = nil
  end
end

class DoublyLinkedList
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
    new_node = DLLNode.new(value)
    if @head
      new_node.prev = find_end
      find_end.next = new_node
    else
      @head = new_node
    end
  end

  def append_after(target, value)
    new_node = DLLNode.new(value)
    target_node = find(target)
    if target_node
      new_node.prev = target_node
      target_node.next.prev = new_node
      new_node.next = target_node.next
      target_node.next = new_node
    end
  end

  def delete(value)
    node = @head
    if node.value == value
      @head.next.prev = nil
      @head = @head.next
      return
    end
    while node
      if node.value == value
        break
      end
      node = node.next
    end
    if node
      node.prev.next = node.next
      if node.next
        node.next.prev = node.prev
      end
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

dll = DoublyLinkedList.new

dll.append("Monday")

dll.append("Wednesday")
dll.append("Thursday")
dll.append_after("Monday", "Tuesday")

dll.print_list
dll.delete("Thursday")
dll.print_list
