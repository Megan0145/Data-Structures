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
                return
            # else recur insert function, this time passing the right node of the current node as the root node (ie self now == self.right)
            else:
                return self.right.insert(value)
        # else new value must fall on LHS of BST (it's LESS than value of the current BST)
        else:
            # if current BST does not have a left node
            if not self.left:
                # add new subtree to the left
                self.left = BinarySearchTree(value)  
                return
            # else recur insert function, this time passing the left node of the current BST as the root node (ie self now == self.left)
            else:
                return self.left.insert(value) 

    
    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # base case: if value of current node is equal to the target value we're looking for
        # BST contains target -> return True
        if self.value == target:
            return True

        # if target is more than the value at the current node we want to continue onto the next node to compare on the RHS
        # can only do that is current node has node to RHS     
        elif target > self.value and self.right:
            # if both conditions true recur function by calling function on the node to the RHS of the current node
            return self.right.contains(target)

        # if target is more than the value at the current node we want to continue onto the next node to compare on the RHS
        # can only do that is current node has node to RHS       
        elif target < self.value and self.left:
            # if both conditions true recur function by calling function on the node to the RHS of the current node
            return self.left.contains(target)
        
        # else we've come to the very last node that the target may possibly reside, return False
        else:
            return False  
            

    # Return the maximum value found in the tree
    def get_max(self):
        # base case: if the current node has no node to the RHS,
        # we must be on the rightmost node of the BST -> return value of node
        if not self.right:
            return self.value
        # else recur the function by calling it on the node to the RHS of the current node til it 
        # reaches base case
        return self.right.get_max()    

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        # firstly call the callback function on the value of the current node
        cb(self.value)
        # if the current node has a node to the RHS (ie self.right is not None)
        if self.right:  
            # recur function on node to RHS
           self.right.for_each(cb)  
        # if the current node has a node to the LHS (ie self.left is not None)    
        if self.left: 
            # recur function on node to LHS 
            self.left.for_each(cb)     

    def dft_for_each_iter(self, cb):
        # create an empty stack
        stack = Stack()
        # push self onto stack
        stack.push(self)
        # iterate over stack
        while stack.len() > 0:
            # pop current node of stack off
            current_node = stack.pop()
            # check if node to left
            if current_node.left:
                # if so push node.left onto stack
                stack.push(current_node.left)
            # check if node to right
            if current_node.right:
                # if so push node.right onto stack  
                stack.push(current_node.right)  
            # invoke callback on current node 
            cb(current_node.value)   

    def bft_for_each_iter(self, cb):
        # create an empty queue
        queue = Queue()
        # enqueue self onto queue
        queue.enqueue(self)
        # iterate over queue
        while queue.len() > 0:
            # dequeue current node of queue off
            current_node = queue.dequeue()
            # check if node to left
            if current_node.left:
                # if so enqueue node.left onto queue
                queue.enqueue(current_node.left)
            # check if node to right
            if current_node.right:
                # if so enqueue node.right onto queue  
                queue.enqueue(current_node.right)  
            # invoke callback on current node 
            cb(current_node.value)           

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        # in order traversal: visit the left branch -> current node -> right branch
        # firstly, check if current node has node to the LHS 
        if node.left:
            # if so, recur function passing in the value of the node to the LHS 
            # this will continue recurring (checking every subtree to LHS of current tree) til it gets to the next smallest element
            self.in_order_print(node.left)
        # then print the value of the current node    
        print(node.value)
        # then check if current node has node to the RHS
        if node.right:
            # if so, recur function passing in the value of the node to the RHS 
            # this will continue recurring (checking every subtree to RHS of current tree) til it gets to the next largest element
            self.in_order_print(node.right)    

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # create an empty queue
        # add starting node to the queue
        
        # iterate over queue
            # set current node to first item in the q
            # then print the current value
            # if the current node has a left child
                # add current left to queue
            # if current right child, 
                # add right child to queue     
        pass
        

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # create an empty stack
        # add starting node to the stack
        
        # iterate over stack
            # set current node to first item in the stack
            # then print the current value
            # if the current node has a left child
                # add current left to stack (push)
            # if current right child, 
                # add right child to stack (push)   
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        # pre-order df traversal: simalar to in-order traversal except the order in which we visit nodes varies slightly
        # we want to visit the current node before visiting any child nodes

        # firstly, print the value of the current node before moving onto the children
        print(node.value)
        # if the current node has a subtree to LHS
        if node.left:
            # recur function on left subtree
            self.pre_order_dft(node.left) 
        # if the current node has a subtree to RHS    
        if node.right:   
            # if the current node has a subtree to RHS 
            self.pre_order_dft(node.right)   

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        # post-order df traversal: simalar to in-order & pre-order traversal except the order in which we visit nodes varies slightly
        # we want to visit the current node LAST, AFTER visiting any child nodes

        # first, if the current node has a subtree to LHS
        if node.left:
            # recur function on left subtree
            self.post_order_dft(node.left) 

        # secondly, if the current node has a subtree to RHS    
        if node.right:   
            # recur function on right subtree
            self.post_order_dft(node.right)   

        # lastly, print the value of the current node
        print(node.value)    

        