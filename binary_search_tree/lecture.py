"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1.  Implement the methods `insert`, `contains`, `get_max`, and `for_each`
    on the BSTNode class.
2.  Implement the `in_order_print`, `bft_print`, and `dft_print` methods
    on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # Case 1: value < root/parent (self.value)
        if value < self.value:
            # If no left child, insert value here
            if self.left is None:
                self.left = BSTNode(value)
            # Else
            else:
                # Repeat this process on Left subtree
                self.left.insert(value)
        # Case 2: value > or = root/parent (self.value)
        if value >= self.value:
            # If no right child, insert value here
            if self.right is None:
                self.right = BSTNode(value)
            # Else
            else:
                # Repeat this process on Right subtree
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # Case 1: self.value = target
        if self.value == target:
            return True
        # Case 2: target < self.value
        if target < self.value:
            # If self.left is None, its not in the tree
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        # Case 3: otherwise
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # DFT!!
        # while self.right != None:
        #     self = self.right
        #     return self.value
        if not self:
            return None
        # Recursion Version:
        # if self.right is None:
        #     return self. value
        # return self.right.get_max()

        max_value = self.value
        current = self
        while current:
            if current.value > max_value:
                max_value = current.value
            current = current.right
        return max_value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # DFT!!
        # fn(self.value)
        # if self.left != None:
        #     self.left.for_each(fn)
        # if self.right != None:
        #     self.right.for_each(fn)
        fn(self.value)

        # Initialize max_value variable
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        # STACK!! --> or use Recursion
        # # pre_order_dft:
        # # recurse Left
        # self.left.fn()
        # # visit logic
        # print(self.value)
        # # recurse Right
        # self.right.fn()
            # # post_order_dft
            # # recurse Left
            # self.left.fn()
            # # recurse Right
            # self.right.fn()
            # # visit logic
            # print(self.value)
        # if the current Node == None:
        #     we know we've reached the end of a recursion/base case
        #     return
        # (base case) we want to return
        if self is None:
            return
        # check if we can "move left"
        if self.left is not None:
            self.left.in_order_print()
        # visit the node by printing its value
        print(self.value)
        # check if we can "move right"
        if self.right is not None:
            self.right.in_order_print()

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass
        # QUEUE!!
        # Not Recursion! Its Iterative! = while loop
        # You should import the queue class from earlier in the
        # week and use that class to implement this method
        # use a queue to form a line for the nodes to line up in
        
        # start by placing the root in the queue
        
        # need a while loop to iterate
        # while length of queue is greater than 0
        #     dequeue item from front of queue
        #     print it

        #     place current item's left node in queue if not None
        #     place current item's right node in queue if not None

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass
        # Initialize an empty STACK
        # push the root node onto the STACK

        # need a while loop to manage iteration
        # if stack is not empty, enter the while loop
        #     pop top item off the STACK
        #     print that item's value

        #     if there is a left subtree
        #         push left item onto the STACK

        #     if there is a right subtree
        #         push right item onto the stack

# Know how to reverse a singly linked list - numpy intersect1d

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass