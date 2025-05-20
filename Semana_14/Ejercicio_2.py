# Double Ended Queue


class Node:
    data : str
    next : "Node"
    prev : "Node"

    def __init__(self, data, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev

class DoubleEndedQueue:

    def __init__(self, head):
        self.head = head
        self.tail = head    

    def print_structure (self):
        current_node = self.head
        print_text = ''
        while (current_node is not None):
            if print_text == '':
                print_text = current_node.data
            else: 
                print_text = print_text + ' <-> ' + current_node.data
            current_node = current_node.next
        print (print_text)

    def push_right (self, new_node):
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node


    def push_left (self, new_node):
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node


    def pop_right (self):

        if self.tail is None:
            print('Queue is empty')
            return None
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None


    def pop_left (self):

        if self.head is None:
            print ('Queue is empty')
            return None

        if self.head:
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

# print("POP LEFT")
# my_DEQ.pop_left()
# my_DEQ.print_structure()

print("POP RIGHT")
my_DEQ.pop_right()
my_DEQ.print_structure()