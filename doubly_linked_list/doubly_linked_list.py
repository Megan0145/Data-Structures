"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        # wrap value in ListNode and initially set next and prev values to None
        new_node = ListNode(value, None, None)
        # if the list currently has no head and no tail (is empty),
        # set the head and the tail to the new node
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            # set the next attribute on the new node equal to the list's current head node    
            new_node.next = self.head
            # set the prev attribute on the list's current head node equal to the new node
            self.head.prev = new_node
            # set the list's head node equal to the new node
            self.head = new_node
        # increment the length of the list by 1
        self.length += 1    

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        # store value of head node so we can return it after deletion
        removed_node = self.head.value
        # call delete method passing in the head node
        self.delete(self.head)
        # return value of node
        return removed_node

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        # wrap value in ListNode and initially set next and prev values to None
        new_node = ListNode(value, None, None)
        # if the list currently has no head and no tail (is empty),
        # set the head and the tail equal to the new node
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            # set the prev attribute on the new node equal to the list's current tail node    
            new_node.prev = self.tail
            # set the next attribute on the list's current tail node equal to the new node
            self.tail.next = new_node
            # set the list's tail node equal to the new node
            self.tail = new_node
        # increment the length of the list by 1
        self.length += 1    

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        # store value of tail node so we can return it after deletion
        removed_node = self.tail.value
        # call delete method passing in the tail node
        self.delete(self.tail)
        # return value of node
        return removed_node

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        # if node is head node it's already at the front - just return from function
        if node is self.head:
            return
        # else store the value of the node in a variable
        value = node.value

        # else if node is list's tail node, call our remove_from_tail function
        if node is self.tail:
            self.remove_from_tail()

        # else the node is somewhere in the middle of our list
        # call our delete function on the node and decrement the length of the list by one 
        # (when we call the add to head function below it will increment the length of the list by one)
        else:
            node.delete()
            self.length -= 1

        # finally, regardless of what conditional statement the node belonged to above (where it was located in the list)
        # call the add_to_head method passing in the value of the node that we have previously store in the 'value' variable
        self.add_to_head(value)

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
         # if node is tail node it's already at the end - just return from function
        if node is self.tail:
            return
        # else store the value of the node in a variable
        value = node.value

        # else if node is list's head node, call our remove_from_head function
        if node is self.head:
            self.remove_from_head()

        # else the node is somewhere in the middle of our list
        # call our delete function on the node and decrement the length of the list by one 
        # (when we call the add to tail function below it will increment the length of the list by one)
        else:
            node.delete()
            self.length -= 1

        # finally, regardless of what conditional statement the node belonged to above (where it was located in the list)
        # call the add_to_tail method passing in the value of the node that we have previously store in the 'value' variable
        self.add_to_tail(value)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        # if there is no head and no tail nodes (list is empty),
        # just return from function - nothing to delete
        if not self.head and not self.tail:
            return

        # if the list's head node == list's tail node (there's only one node in list)
        # just set them both equal to None
        if self.head is self.tail:
            self.head = None
            self.tail = None    

        # else if the node we want to delete is the list's head node
        # set the head node equal to the next node and delete the node (using delete method in ListNode class)    
        elif node is self.head:
            # could also say: self.head = self.head.next
            self.head = node.next
            node.delete()

        # else if the node we want to delete is the list's tail node
        # set the tail node equal to the prev node and delete the node 
        elif node is self.tail:
            # could also say: self.tail = self.tail.prev
            self.tail = node.prev
            node.delete()

        # else node is somewhere in middle of list - 
        # just delete the node using delete method in ListNode class 
        # which will handle updating the pointers on the next and prev nodes accordingly
        else:
            node.delete()

        # decrement length of list
        self.length -= 1


    """Returns the highest value currently in the list"""
    def get_max(self):
        # if list has no head node (is empty), there will be no max value - just return from function
        if not self.head:
            return None
        # else set the initial max value in list equal to value of head node 
        # and declare variable to hold the current node, initalize it to head node 
        # (equivalent to if we were iterating over an array using a for loop and incrementing value of i on each iteration - current_node = node at index i)
        max_val = self.head.value
        current_node = self.head
        # while current_node is not None (we haven't reached the end of the list)
        while current_node:
            # if the value of the current node is bigger than the max_val
            if current_node.value > max_val:
                # set max_val equal to value at current node
                max_val = current_node.value
                # move on to the next node in the list
            current_node = current_node.next
        # when we reach the end of the list (the while loop has finished executing), return the max_val    
        return max_val        
