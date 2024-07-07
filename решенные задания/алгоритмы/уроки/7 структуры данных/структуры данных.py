from time import sleep 
                                                    #очередь
# # class Queue:
# #     def __init__(self) -> None:
# #         self.el = list()
        
# #     def add(self, value):
# #         self.el.append(value)
    
# #     def get(self):
# #         val = self.el.pop(0)
# #         return val
    
# #     def size(self):
# #         size = len(self.el)
# #         return size
    
# class Queue:
#     def __init__(self) -> None:
#         self.el = list()
        
#     def add(self, value):
#         self.el.insert(0, value)
    
#     def get(self):
#         val = self.el.pop()
#         return val
    
#     def size(self):
#         size = len(self.el)
#         return size  

# queue = Queue()
# for i in range(10):
#     queue.add(i)
    
# for i in range(queue.size()):
#     val = queue.get()
#     print(val)
#     sleep(val)

                                                    #стек
class Stack:
    def __init__(self) -> None:
        self.el = list()
        
    def add(self, value):
        self.el.insert(0, value)
        # self.el.append(value)
    
    def get(self):
        # val = self.el.pop()
        val = self.el.pop(0)
        return val
    
    def size(self):
        size = len(self.el)
        return size  
    
queue = Stack()
for i in range(9, -1, -1):
    queue.add(i)
    print(i, end=' ')
print()
    
for i in range(queue.size()):
    val = queue.get()
    print(val)
    sleep(val)