class Node:
    def __init__(self,value) -> None:
        self.value = value
        self.next = None

class Stack:
    def __init__(self,value) -> None:
        self.head = Node(value)
        self.next = None
        self.prev = None
        self.length = 1    

    def push(self,value):

        new_node = Node(value)
        pass
