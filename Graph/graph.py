#undirected , unweighted graph (adjacency list)

"""
-fields :
        1-vertices number
        2-edges number 
        3-adjacency list
-methods :
        1-add node
        2-connect two nodes
        3-delete a node
        4-print 
        5-get v ( vertices , supposing v and e are private fields)
        6-get e  (edges :private field)
        7-disconnect two nodes
        

"""


class AL_Graph:
    def __init__(self):
        self.v = 0
        self.e = 0
        self.adjacency_list = {}

    def add_node(self , name):
        self.adjacency_list[name] = []
        self.v+=1

    def connect_two_nodes(self , name1 , name2):
        if name1 in self.adjacency_list and name2 in self.adjacency_list:
            self.adjacency_list[name1].append(name2)
            self.adjacency_list[name2].append(name1)
            self.e+=1
        else:
            print("one or both of the vertices are not in the graph")
    def disconnect_two_nodes(self , name1 , name2):  #assuming name1 and name2 are already connected
        if name1 in self.adjacency_list and name2 in self.adjacency_list:
            self.adjacency_list[name1].remove(name2)
            self.adjacency_list[name2].remove(name1)
            self.e-=1
        else:
            print("one or both of the nodes are not in the graph")
        
    def get_v(self):
        return self.v

    def print(self):
        for key in self.adjacency_list.keys():
            print(key , end="->")
            for item in self.adjacency_list[key]:
                print(item ,end = " ")
            print("")
    def get_e(self):
        return self.e

    def remove_node(self,  name):
        to_be_moded = []
        for item in self.adjacency_list[name]:
            to_be_moded.append(item)
        del self.adjacency_list[name]
        for mod in to_be_moded:
            self.adjacency_list[mod].remove(name)
        self.v-=1
        self.e -= len(to_be_moded)

