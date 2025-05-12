# Double Ended Queue


class Node:
    data : str
    next : "Node"

    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class DoubleEndedQueue:
    head = Node
    # tail = Node

    def __init__(self, head):
        self.head = head
        # self.tail = None

    def print_structure (self):
        current_node = self.head
        while (current_node is not None):
            print (current_node.data)
            current_node = current_node.next
    
    def push_right (self, new_node):
        current_node = self.head
        while (current_node.next is not None):
            current_node = current_node.next
        current_node.next = new_node


    def push_left (self, new_node):
        if (self.head is None):
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def pop_right (self):
        
        if (self.head is None):
            return None
        if (self.head.next is None):
            self.head = None
            return None
        current_node = self.head
        while (current_node.next.next is not None):
            current_node = current_node.next
        current_node.next = None

    def pop_left(self):
        if (self.head):
            self.head = self.head.next

first_node = Node("First")
my_DEQ = DoubleEndedQueue(first_node)

second_node = Node("Second")
third_node = Node("Third")
forth_node = Node("forth")

my_DEQ.print_structure()

print("PUSH LEFT")
my_DEQ.push_left(second_node)
my_DEQ.print_structure()

print("PUSH RIGHT")
my_DEQ.push_right(third_node)
my_DEQ.print_structure()

print("PUSH LEFT")
my_DEQ.push_left(forth_node)
my_DEQ.print_structure()

print("POP RIGHT")
my_DEQ.pop_right()
my_DEQ.print_structure()

print("POP LEFT")
my_DEQ.pop_left()
my_DEQ.print_structure()