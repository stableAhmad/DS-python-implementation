class Q:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def add(self , val):
        new_node = Node(val , None)
        if( not self.head):
            self.head = new_node
            self.tail = new_node
            return
        new_node.next=  self.tail
        self.tail = new_node
        self.size +=1

    def print(self):
        current = self.tail
        while(current):
            print(current.val)
            current = current.next
    def de_q(self):
        if(self.size == 0):
            print("nothing to delete")
            return
        print(self.head)
        self.head = None
        current = self.tail
        while(current):
            if current.next == None:
                self.head = current
            else:
                current = current.next
        self.size-=1 






class Node:
    def __init__(self , val , next_node):
        self.val = val
        self.next = next_node


   

test = Q()
test.add(1)
test.add(2)
test.add(3)
test.add(4)
test.print()














