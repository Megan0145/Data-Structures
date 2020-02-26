import sys
sys.path.append('../queue_and_stack')
# from dll_queue import Queue
# from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # check if new value will fall on RHS of value of current BST (is it MORE than OR EQUAL to the root node of the current BST)
        if value >= self.value:
            # if current BST does not have a right node
            if not self.right:
                # add new subtree to the right 
                self.right = BinarySearchTree(value)
                # return from function
                return
            # else recur insert function, this time passing the right node of the current node as the root node (ie self now == self.right)
            return self.right.insert(value)

        # else new value must fall on LHS of BST (it's LESS than value of the current BST)
        else:
            # if current BST does not have a left node
            if not self.left:
                # add new subtree to the left
                self.left = BinarySearchTree(value)
                # return from function
                return
            # else recur insert function, this time passing the left node of the current BST as the root node (ie self now == self.left)
            return self.left.insert(value) 
    
    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        pass

    # Return the maximum value found in the tree
    def get_max(self):
        pass

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        pass

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
