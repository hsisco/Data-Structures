"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev         
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        new_node = ListNode(value)
        self.length += 1
        # if self.head is None:
        if not self.tail and not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            # temp = self.head
            new_node.prev = self.head
            self.head.next = new_node
            self.head = new_node
            # temp.prev = self.head
            # self.head.next = temp
        # self.length +=1

    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        new_node = ListNode(value)
        self.length += 1
        # if self.head is None:
        if not self.tail and not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            # temp = self.head
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            # temp.prev = self.tail
            # self.tail.next = temp
        # self.length +=1

    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        value = self.head.value
        self.delete(self.head)
        return value
        # if self.head is None:
        #     return None
        #
        # self.length -= 1
        # if self.head.next is None:
        #     head = self.head
        #     self.head = None
        #     self.tail = None
        #     return head.value
        #
        # value = self.head.value
        # self.head = self.head.next
        # self.head.prev = None
        # return value

    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        value = self.tail.value
        self.delete(self.tail)
        return value
        # if self.head is None:
        #     return None
        #
        # self.length -= 1
        # if self.head.next is None:
        #     head = self.head
        #     self.head = None
        #     self.tail = None
        #     return head.value
        #
        # tail = self.tail
        # self.tail.prev.next = None
        # self.tail = self.tail.prev
        # tail.prev = None
        # return tail.value

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        if node is self.head:
            return
        value = node.value
        if node is self.tail:
            self.remove_from_tail()
        else:
            node.delete()
            self.length -= 1
        self.add_to_head(value)

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if node is self.tail:
            return
        value = node.value
        if node is self.head:
            self.remove_from_head()
        else:
            node.delete()
            self.length -= 1
        self.add_to_tail(value)

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        if not self.head and not self.tail:
            return
        
        self.length -= 1
        if self.head == self.tail:
            self.head = None
            self.tail = None
        elif self.head == node:
            self.head = node.next
            node.delete()
        elif self.tail == node:
            self.tail = node.prev
            node.delete()
        else:
            node.delete()

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        curr = self.head
        max_value = curr.value
        while curr is not None:
            if curr.value > max_value:
                max_value = curr.value
            curr = curr.next
        
        return max_value