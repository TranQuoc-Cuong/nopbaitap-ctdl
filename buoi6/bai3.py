class Node:
  def __init__(self, data):
      self.data = data
      self.next = None

class LinkedList:
  def __init__(self):
      self.head = None

  def append(self, new_data):
      new_node = Node(new_data)
      if self.head is None:
          self.head = new_node
      else:
          current = self.head
          while current.next:
              current = current.next
          current.next = new_node

  def display(self):
      current = self.head
      while current:
          print(current.data, end=" -> ")
          current = current.next
      print("None")

if __name__ == "__main__":
  linked_list = LinkedList()
  linked_list.append(2)
  linked_list.append(3)
  linked_list.append(4)
  linked_list.append(5)

  print("danh sach ban dau")
  linked_list.display()

  new_element = 1
  linked_list.append(new_element)

  print("danh sach sau khi duoc chen", new_element, "vao cuoi")
  linked_list.display()