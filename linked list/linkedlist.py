#element means node
class Element:
    def __init__(self,value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, head =None) -> None:
        self.head = head
        self.next = None


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


    #method to insert element into linked list
    def insert(self,new_element,positon):
        counter = 1
        current = self.head

        if positon > 1:
            while current and counter < positon:
                if counter == positon - 1:
                    new_element.next = current.next
                    current.next = new_element
                current = current.next
                counter += 1
        elif positon == 1:
            new_element.next =  self.head
            self.head = new_element

    #method to delete an element 
    def delete(self,value):
        current = self.head
        previous = None
        while current.value != value and current.next:
            previous = current
            current = current.next
        
        if current.value == value:
            if previous:
                previous.next = current.next
            else:
                self.head = current.next

e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

# Test get_position
# Should print 3
print(ll.head.next.next.value)
# Should also print 3
print(ll.get_position(3).value)

# Test insert
ll.insert(e4,3)
# Should print 4 now
print(ll.get_position(3).value)

# Test delete
ll.delete(1)
# Should print 2 now
print(ll.get_position(1).value)
# Should print 4 now
print(ll.get_position(2).value)
# Should print 3 now
print(ll.get_position(3).value)