# 1        we need to create a class create node


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
        return True             #not really necessary

    def pop(self):
        temp = self.head
        pre = self.head

        if self.length == 0:
            return None

        while temp.next:
            pre = temp
            temp = temp.next
        pre.next = None  # or write code belwo
        self.tail = pre
        #self.tail.next = None
        self.length -= 1  # when this becomes 0 then
        if self.length == 0:        #if there exit only one node in the lis
            self.head = None
            self.tail = None
        return temp.value

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        self.length -= 1
        if self.length == 0:        # edge case
            self.tail = temp
        return temp.value

    def prepend(self , value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def get_index(self,index):
        temp = self.head
        if index <0 or index >= self.length:
            return None
        for _ in range(index):
            temp = temp.next
        return temp

    def set_index(self,index,value):
        temp = self.get_index(index)
        if temp:
            temp.value = value
            return True
        return False
        
    def insert(self,index ,value):
        new_node = Node(value)
        temp = self.get_index(index - 1)
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

    def remove(self,index):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.pop_first()
        if index == self.length:
            return self.pop()
        prev = self.get_index(index -1)
        temp = prev.next                    #  temp =  get_index(index) more efficient way    since get index ha O(n)
        prev.next = temp.next
        temp.next = None
        self.length -=1
        return temp

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value , end=" -> ")
            temp = temp.next
        print("END")
    
    def reverse(self):
        # first switch head and tail
        temp = self.head
        self.head = self.tail
        self.tail = temp
        # create variables that points before and after the head
        after = temp.next
        before = None

        #main reversing order
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after    



# 3            to create a linked list 

# testing code
my_linked_list = LinkedList(4)
my_linked_list.append(2)
my_linked_list.append(3)



my_linked_list.append(45)
my_linked_list.print_list()

print("poped item is :",my_linked_list.pop())

my_linked_list.print_list()

my_linked_list.prepend(998)


my_linked_list.print_list()

my_linked_list.set_index(3,112)

my_linked_list.print_list()

my_linked_list.insert(2,0)

my_linked_list.print_list()

my_linked_list.reverse()

my_linked_list.print_list()

# printing linked list
