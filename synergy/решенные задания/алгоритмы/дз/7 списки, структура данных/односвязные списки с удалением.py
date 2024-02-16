import random
class Node:
    def __init__(self):
        self.val = None
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = Node()
        self.start = None
        self.fin = None
        
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
        
    def delete(self, val):
        if ll.find(val) == False:
            print('Такого элемета в списке нет')
        curent_node = self.head
        if self.head.val is not None:
            if self.head.val == val:
                self.head.val = None
        while curent_node is not None:
            if curent_node.val == val:
                break
            temp = curent_node
            curent_node = curent_node.next
        if curent_node == None:
            return
        temp.next = curent_node.next
        curent_node = None
        
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
        print()
            
    # def sort(self):
    #     curent_node = self.head
    #     tmp = True
    #     tmp_next = 0
    #     tmpn = 0
    #     while(tmp):
    #         tmp = False
    #         for i in range(ll.length() - tmpn - 1):
    #             while curent_node.next is not None:
    #                 print(curent_node.val , curent_node.next.val)
    #                 if curent_node.val > curent_node.next.val:
    #                     tmp_next = curent_node
    #                     curent_node = curent_node.next
    #                     curent_node.next = tmp_next
    #                     tmp = True
    #                 else:
    #                     curent_node = curent_node.next
    #             tmpn += 1
    #     if tmpn == 1:
    #         print("список не требует сортирвки ")
    #     return                
    
    
ll = LinkedList()

ll.add(3)
ll.add(7)
ll.add(6)
ll.add(7)
ll.add(8)
ll.add(9)
# ll.delete(34)
# ll.sort()
ll.print()