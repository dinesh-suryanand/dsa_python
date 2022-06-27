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
    def insert(self, new_element, position):
        counter = 1
        current = self.head
        if position > 1:
            while current and counter < position:
                if counter == position - 1:
                    new_element.next = current.next
                    current.next = new_element
                current = current.next
                counter += 1
        elif position == 1:
            new_element.next = self.head
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

    # method to display            
    def display(self):
        current = self.head
        while current != None:
            print(current.value , end= " -> ")
            current = current.next
        print("END")
    


e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)
e5 = Element(97)
e6 = Element(69)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)
ll.append(e4)
ll.append(e6)
ll.append(e5)
# print(ll.get_position(3).value)
ll.append(e2)

ll.display()

print(e5.next)


# ll.display()


