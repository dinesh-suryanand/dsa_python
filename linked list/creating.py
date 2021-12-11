from os import curdir


class Element:
    def __init__(self,value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, head =None) -> None:
        self.head = head

    #method to add elements to linked list
    def append(self , new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element
    
    #metod to get position of an element
    def get_position(self,position):
        pass