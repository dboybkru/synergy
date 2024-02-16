# Узел связанного списка
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
 
 
# Функция для печати заданного связанного списка
def printList(head):
 
    ptr = head
    while ptr:
        print(ptr.data, end=' —> ')
        ptr = ptr.next
    print('None')
 
 
# Берет два списка, отсортированных по возрастанию, и объединяет их узлы
#, чтобы сделать один большой отсортированный список, который возвращается
def sortedMerge(a, b):
 
    # Базовые варианты
    if a is None:
        return b
    elif b is None:
        return a
 
    # выбирает `a` или `b` и повторяет
    if a.data <= b.data:
        result = a
        result.next = sortedMerge(a.next, b)
    else:
        result = b
        result.next = sortedMerge(a, b.next)
 
    return result
 
 
'''
    Split the given list's nodes into front and back halves,
    If the length is odd, the extra node should go in the front list.
    It uses the fast/slow pointer strategy
'''
 
 
def frontBackSplit(source):
 
    #, если длина меньше 2, обрабатывается отдельно
    if source is None or source.next is None:
        return source, None
 
    (slow, fast) = (source, source.next)
 
    # продвигает `fast` на два узла и продвигает `slow` на один узел
    while fast:
 
        fast = fast.next
        if fast:
            slow = slow.next
            fast = fast.next
 
    # `slow` находится перед средней точкой списка, поэтому разделите его на две части.
    # на тот момент.
    ret = (source, slow.next)
    slow.next = None
 
    return ret
 
 
# Сортировка заданного связанного списка с использованием алгоритма сортировки слиянием
def mergesort(head):
 
    # Базовый случай — длина 0 или 1
    if head is None or head.next is None:
        return head
 
    # разделить `head` на подсписки `a` и `b`
    front, back = frontBackSplit(head)
 
    # рекурсивно сортирует подсписки
    front = mergesort(front)
    back = mergesort(back)
 
    # ответ = объединить два отсортированных списка
    return sortedMerge(front, back)
 
 
if __name__ == '__main__':
 
    # Клавиши ввода
    keys = [8, 6, 4, 9, 3, 1]
 
    head = None
    for key in keys:
        head = Node(key, head)
 
    # сортировать список
    head = mergesort(head)
 
    # распечатать отсортированный список
    printList(head)