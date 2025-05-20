# Stack

class Node:
    data : str
    next : "Node"

    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class Stack:
    top = Node

    def __init__(self, top):
        self.top = top

    def print_structure (self):
        current_node = self.top
        while (current_node is not None):
            print (current_node.data)
            current_node = current_node.next
    
    # def push_node (self, new_node):
    #     current_node = self.top
    #     while (current_node.next is not None):
    #         current_node = current_node.next
    #     current_node.next = new_node

    def push_node (self, new_node):
        new_node.next = self.top
        self.top = new_node

    # def pop_node (self):
        
    #     if (self.top is None):
    #         return None
    #     if (self.top.next is None):
    #         self.top = None
    #         return None
    #     current_node = self.top
    #     while (current_node.next.next is not None):
    #         current_node = current_node.next
    #     current_node.next = None

    def pop_node (self):
        
        if (self.top is None):
            print ('Stack is empty')
            return None
        if (self.top.next is None):
            self.top = None
            return None
        
        self.top = self.top.next


first_node = Node("First")
my_stack = Stack(first_node)

second_node = Node("Second")
my_stack.push_node(second_node)

third_node = Node("Third")
my_stack.push_node(third_node)

forth = Node("forth")
my_stack.push_node(forth)

my_stack.print_structure()

print("POP NODE")

my_stack.pop_node()
my_stack.print_structure()

print("POP NODE")

my_stack.pop_node()
my_stack.print_structure()

print("POP NODE")

my_stack.pop_node()
my_stack.print_structure()

print("POP NODE")

my_stack.pop_node()
my_stack.print_structure()


print("POP NODE")

my_stack.pop_node()
my_stack.print_structure()