
class Node:
    def __init__(self):
        self.val = None
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = Node()
        
    def add(self, val):
        if self.head.val is None:
            self.head.val = val
            return
        
        temp = Node()
        temp.val = val
        #1 вариант
        # curent_node = self.head
        # while curent_node.next is not None:
        #     curent_node = curent_node.next
        # curent_node.next = temp
        #2 вариант
        temp.next = self.head
        self.head = temp
        
    def length(self):
        curent_node = self.head
        if self.head.val is None:
            size = 0
        else:
            size = 1
        while curent_node.next is not None:
            curent_node = curent_node.next
            size += 1
        return size
    
    def find(self, val):
        curent_node = self.head
        if self.head.val is not None:
            if self.head.val == val:
                return True
        curent_node = self.head
        while curent_node.next is not None:
            curent_node = curent_node.next
            if curent_node.val == val:
                return True
        return False
    
    def print(self):
        if self.head.val is None:
            print('Список пустой')
            return
        print(self.head.val, end=' ')
        curent_node = self.head
        while curent_node.next is not None:
            curent_node = curent_node.next
            print(curent_node.val, end=' ')
            # curent_node = curent_node.next
        print()
            
    def get(self):
        pass
    
    
ll = LinkedList()
print(ll.length())
ll.print()
print(ll.find(0), ll.find(9), ll.find(6))
ll.add(9)
print(ll.length())
ll.print()
print(ll.find(0), ll.find(9), ll.find(6))
ll.add(7)
print(ll.length())
ll.print()
print(ll.find(0), ll.find(9), ll.find(6))
ll.add(6)
print(ll.length())
ll.print()
print(ll.find(0), ll.find(9), ll.find(6))
ll.add(4)
print(ll.length())
ll.print()
print(ll.find(0), ll.find(9), ll.find(6))
ll.add(9)
print(ll.length())
ll.print()
print(ll.find(0), ll.find(9), ll.find(6))
ll.add(0)
print(ll.length())
ll.print()
print(ll.find(0), ll.find(9), ll.find(6))
a= 10
ll.print()