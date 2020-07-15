"""
First In, First Out (FIFO):
- queue
- Methods / Behaviors / Operations:
    enqueue(item) - add item to the end of the line
    dequeue() - remove item at the begining of the line (typically returns removed item)

A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1.  Implement the Queue class using an array as the underlying storage structure.
    Make sure the Queue tests pass.
2.  Re-implement the Queue class, this time using the linked list implementation
    as the underlying storage structure.
    Make sure the Queue tests pass.
3.  What is the difference between using an array vs. a linked list when 
    implementing a Queue?
    
Stretch:    What if you could only use instances of your Stack class to implement the Queue?
            What would that look like? How many Stacks would you need? Try it!
"""
import sys
sys.path.append('../singly_linked_list')
from singly_linked_list import LinkedList

# class Queue:
#     def __init__(self):
#         self.storage = []
    
#     def __len__(self):
#         return len(self.storage)

#     def enqueue(self, value):
#         self.storage.insert(0, value)

#     def dequeue(self):
#         if len(self.storage) < 1:
#             return None
#         return self.storage.pop()
class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()
    
    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.storage.add_to_head(value)
        self.size += 1

    def dequeue(self):
        removed = self.storage.remove_tail()
        if removed is not None:
            self.size -= 1
        return removed