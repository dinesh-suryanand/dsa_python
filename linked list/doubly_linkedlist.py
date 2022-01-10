class Element:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self, head =None) -> None:
        self.head = head
        self.next = None
        self.prev = None


    #methood to append element in linked list
    def append(self,new_element):
        node = self.head
        if self.head:
            while node.next:
                node = node.next
            node.next = new_element
            new_element.prev = node
        else:
            self.head = new_element


    #metod to get position of an element
    def get_position(self,position):
        counter = 1
        current = self.head
        
        if position < 1:
            return None

        while current and counter <= position:
            if counter == position:
                return current
            current = current.next
            counter += 1

        return None


    #method to add element in doubly linked list
    #this code is not tested yet
    def insert(self,position,insert_node):
        curret_node = self.get_position(position)
        next_node = curret_node.next
        insert_node.next = curret_node.next
        insert_node.prev = curret_node
        curret_node.next = insert_node
        
