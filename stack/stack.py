from traceback import print_stack
from turtle import st


class Node:
    def __init__(self,value) -> None:
        self.value = value
        self.next = None

class Stack:
    def __init__(self,value) -> None:
        new_node = Node(value)
        self.top = new_node
        self.length = 1    

    def print_stack(self):
        current_node = self.top
        while current_node:
            print(current_node.value , end=" | ")
            current_node = current_node.next
        print()

    def push(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
            self.length += 1
    
    def pop(self):
        if self.length ==0:
            return None
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.length -=1
        return temp

        


my_stack = Stack(4)

my_stack.print_stack()

my_stack.push(77)
my_stack.push(9)
my_stack.push(27)

my_stack.print_stack()
