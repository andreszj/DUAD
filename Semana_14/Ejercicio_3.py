# # BINARY TREE

class Node:
    data: str
    left: "Node"
    right: "Node"

    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self, root):
        self.root = root

    def print_structure(self, node = None):
        if self.root is None:
            print('Binary Tree is empty')

        if node is None:
            node = self.root
        
        if node is not None:
            print(node.data)  
            if node.left is not None:
                self.print_structure(node.left)  
            if node.right is not None:
                self.print_structure(node.right)  

first_node = Node("First")
second_node = Node("Second")
third_node = Node("Third")
forth_node = Node("Forth")

my_Binary_Tree = BinaryTree(first_node)


first_node.left = second_node
first_node.right = third_node
second_node.left = forth_node

my_Binary_Tree.print_structure()
