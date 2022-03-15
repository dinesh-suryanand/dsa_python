class Node:
    def __init__(self,value) -> None:
        self.value = value
        self.next = None
        self.prev = None


class Dll:
    def __init__(self,value) -> None:
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def append(self,value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = temp.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp

    def  prepend(self,value):            
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True
    
    def pop_first(self):
        if self.head == 0:
            return None 
        temp = self.head
        if self.head == 1:
            self.head = None
            self.tail = None
        else:
            self.head = temp.next
            temp.next = None
            temp.prev = None

    def get_index(self,index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        if index <= self.length/2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length -1,index , -1):
                temp = temp.prev
        return temp

    def set_value(self,index,value): 
        temp = self.get_index(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self,index,value):
        if index < 0 and index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)

        new_node = Node(value)
        before = self.get_index(index -1)

        after = before.next
        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev = new_node
        
        self.length += 1
        return True
    
    def remove(self,index):
        if index < 0 and index >= self.length:
            return False
        if index == 0:
            return self.pop_first()
        if index == self.length-1:
            return self.pop()
        
        temp = self.get_index(index)
        temp.prev.next = temp.next
        temp.next.prev = temp.prev
        temp.next = None
        temp.prev = None

        self.length -= 1
        return temp
    
        
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value , end=" -> ")
            temp = temp.next
        print("END")



# TESTING CODE
doubly_linked_list = Dll(1)
doubly_linked_list.append(2)
doubly_linked_list.append(3)

doubly_linked_list.print_list()

doubly_linked_list.prepend(0)

doubly_linked_list.print_list()

doubly_linked_list.pop_first()

doubly_linked_list.print_list()

doubly_linked_list.set_value(1,24)

doubly_linked_list.print_list()

doubly_linked_list.insert(1,3333)

doubly_linked_list.print_list()

doubly_linked_list.remove(2)

doubly_linked_list.print_list()

