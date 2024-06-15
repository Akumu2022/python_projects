class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    

class LinkedList:
    def __init__(self):
        self.head=None
        
    def insert(self,newNode):
        if self.head is None:
            self.head=newNode


node_1=Node("John")
linkedList_1=LinkedList()
linkedList_1.insert(node_1)

node_2=Node("John")
linkedList_2=LinkedList()
linkedList_2.insert(node_2)

