class Node:
    def __init__(self):
        self.val = None
        self.next = None
        self.prev = None
        
class DoubleLnkedList():
    def __init__(self):
        self.head = Node()
        
    def ins_to_end(self, val):
        if self.head.val is None:
            self.head.val = val
            return
        curent_node = self.head
        while curent_node.next is not None:
            curent_node = curent_node.next
        temp = Node()
        temp.val = val
        temp.prev = curent_node
        curent_node.next = temp
        
    
    def ins_to_start(self, val):
        if self.head.val is None:
            self.head.val = val
            return
        temp = Node()
        temp.val = val
        temp.next = self.head
        self.head.prev = temp
        self.head = temp
    
    def ins_after_val(self, after_val, val_to_ins):
        if self.head.val is None:
            raise Exception('Empty list')
        if self.head.val == after_val:
            temp = Node()
            temp.val = val_to_ins
            temp.next = self.head.next
            temp.prev = self.head
            self.head.next.prev = temp
            self.head.next = temp
            return
        curent_node = self.head
        while curent_node.next is not None:
            if curent_node.val == after_val:
                break
            curent_node = curent_node.next
        if curent_node.next is None:
            if curent_node.val != after_val:
                raise Exception('No such element')
        temp = Node()
        temp.val = val_to_ins
        temp.next = curent_node.next
        temp.prev = curent_node
        curent_node.next.prev = temp
        curent_node.next = temp
        
    def del_from_end(self):
        if self.head.val is None:
            raise Exception('Empty list')
        if self.head.next is None:
            val = self.head.val
            self.head = Node()
            return val
        curent_node = self.head
        while curent_node.next is not None:
            curent_node = curent_node.next
        val = curent_node.val
        curent_node.prev.next = None
        return val
    
    def del_from_start(self):
        if self.head.val is None:
            raise Exception('Empty list')
        if self.head.next is None:
            val = self.head.val
            self.head = Node()
            return val
        self.head.next.prev = None
        val = self.head.val
        self.head = self.head.next
        return val
                
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
    
dll = DoubleLnkedList()
# dll.ins_to_end(9)
# dll.ins_to_end(7)
# dll.ins_to_end(6)
# dll.ins_to_end(4)
# dll.ins_to_start(9)
# dll.ins_to_start(7)
# dll.ins_to_start(6)
# dll.ins_to_start(4)
dll.ins_to_start(9)
dll.print()
dll.ins_to_end(5)
dll.print()
dll.ins_to_start(6)
dll.print()
dll.ins_after_val(9, 8)
dll.print()
a = 10

print(dll.del_from_end())
print(dll.del_from_start())
print(dll.del_from_end())
print(dll.del_from_start())
print(dll.del_from_end())
print(dll.del_from_start())
print(dll.del_from_end())
print(dll.del_from_start())
dll.print()