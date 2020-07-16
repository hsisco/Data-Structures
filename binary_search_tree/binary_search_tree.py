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
        while self.right is not None:
            self = self.right
        return self.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        if self.left is not None:
            self.left.for_each(fn)
        if self.right is not None:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if self is None:    # if there's nothing there OR the recursion has run out:
            return              # stop everything and go no further

        if self.left is not None:   # if None doesn't stop us from going left:
            self.left.in_order_print(node)  # use the recursion to get over to that node

        print(self.value)           # print what you find
        
        if self.right is not None:  # if None doesn't stop us from going right:
            self.right.in_order_print(node) # use the recursion to get over to that node
        # And round we go again

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        new_queue = []                              # instantiate queue
        new_queue.append(node)                      # push root node to queue
        while len(new_queue) > 0:                   # while loop to iterate over queue as long as there is someting in it
            print(new_queue[0].value)               # print it that item's value based on:
            if new_queue[0].left is not None:       # if the left node is not None
                new_queue.append(new_queue[0].left)     # push it to the queue
            if new_queue[0].right is not None:      # if the right node is not None
                new_queue.append(new_queue[0].right)    # push it to the queue
            new_queue.pop(0)                        # remove first item in line
        # AGAIN FROM THE TOP!

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        new_stack = []                              # instantiate stack
        new_stack.append(node)                      # push root node to stack
        while len(new_stack) > 0:                   # while loop to iterate over stack as long as there is someting in it
            curr = new_stack.pop()                  # pop top item off stack
            print(curr.value)                       # print that item's value based on:
            if curr.right is not None:              # if there is a left subtree:
                new_stack.append(curr.right)            # push left item onto the stack
            if curr.left is not None:               # if there is a right subtree:
                new_stack.append(curr.left)             # push right item onto the stack
        # AGAIN FROM THE TOP!

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    # def pre_order_dft(self, node):
    #     pass

    # # Print Post-order recursive DFT
    # def post_order_dft(self, node):
    #     pass