from multiprocessing.sharedctypes import Value


class Node:
    def __init__(self,value) -> None:
        self.value = value
        self.next = None

class Queue:
    def __init__(self,value) -> None:
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print_queue(self):
        current_node = self.first
        while current_node:
            print(current_node.value , end=" | ")
            current_node = current_node.next
        print()
    
    def enqueue(self,value):
        new_node = Node(value)
        if self.first is None:            #self.length == 0:
            self.first = new_node
            self.last = new_node 
        else:
            self.last.next = new_node
            self.last = new_node 
        self.length += 1

    def dequeue(self):
        if self.length == 0:
            return None
        temp = self.first

        if self.length == 1:
            self.first = None
            self.last = None
        
        else:
            self.first = self.first.next
            temp.next = None
        self.length -=1
        return temp
        

my_queue = Queue(5)

my_queue.print_queue()

my_queue.enqueue(34)
my_queue.enqueue(99)

my_queue.print_queue()

my_queue.dequeue()

my_queue.print_queue()

my_queue.enqueue(0)

my_queue.print_queue()
