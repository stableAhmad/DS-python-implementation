"""
ADS :
    insert()                done    
    delete()
    get_tree_height()
    traversal :
        in order
        pre order
        post order
    level traversal
        print
    get_size()              done        tested
    get_node_depth()
    get_node_height()

"""
class BST:

    def __init__(self):
        self.root = None
        self.size = 0

    def get_root(self):
        return self.root

    def insert(self , val):
        new_node = Node()
        new_node.val = val
        root = self.get_root()
        if root :
            current = root
            while(True):
                if(new_node.val < current.val):
                    if(current.left):
                        current = current.left
                    else:
                        current.left = new_node
                        break
                else:
                    if(current.right):
                        current = current.right
                    else:
                        current.right = new_node
                        break

        else:
            self.root = new_node
        self.size+=1

    def get_size(self):
        return self.size
    def in_order_traversal(self):
        self.in_recursion(self.root)

    def in_recursion(self , node):
        if not node:
            return
        self.in_recursion(node.left)
        print(node.val , end=" ")
        self.in_recursion(node.right)
class Node:
    def __init__(self):
        self.val = 0
        self.left = self.right = None

   
