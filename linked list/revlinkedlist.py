class Node:
    def __init__(self,value) -> None:
        self.value = value
        self.next = None


class LinkedList:
    # 2         we need a template to create a node
    def __init__(self,value) -> None:
        new_node = Node(value)  # create new node
        self.head = new_node    # makes that node as head
        self.tail = new_node    # makes that node as tail
        self.length = 1

    def append(self,value):
        temp = self.head
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node 
        else :
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def display(self):
        temp = self.head
        while temp:
            print(temp.value, end="->")
            temp = temp.next
        print()
    
    def rev(self):
        crr = self.head.next
        prv =None
        nxt = crr.next
        
        while nxt:
            nxt = crr.next
            crr.next = prv
            prv = crr
            crr = nxt



 
 
ll = LinkedList(1)

ll.append(2)
ll.append(3)
ll.append(4)

ll.rev()
ll.display()
