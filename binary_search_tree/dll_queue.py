import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        
        # As I mentioned below, queues operate on a FIFO basis. So when we add an item to the queue it gets added 
        # to the bottom of the queue (the tail) and when we remove an item from the queue it gets removed from the top (the head).
        # Our DLL is a good choice to store our elements because insertion and deletion are fairly inexpensive in terms of 
        # time complexity. For example, to implement the dequeue method and remove the item at the top of the queue, we just need to
        # set the second item in our DLL's 'prev' attribute equal to none and delete the head node.
        # Inserting at the bottom of queue (enqueueing) is similarly as inexpensive - it's just a matter of readjusting the reference pointers.
        # If we contrast this with using an array as our method of storage, for example, if we are to implement the dequeue method and remove the item at
        # the top of the queue, the index of every item after that item would have be adjusted (decremented by one because we've just removed the 0th item)
        # which increases time complexity.  
  
        self.storage = DoublyLinkedList()

    # Because queues operate according to First In First Out ordering, 
    # the enqueue method will add the item to the end of the queue and increment the size of the queue by one.
    # Much like a queue in real life, when you want to join the queue you join from the end.
    # This can be done by calling the add_to_tail method in our DLL class, passing in the value we want to add.
    def enqueue(self, value):
        self.storage.add_to_tail(value)
        self.size += 1

    # The dequeue method will remove the item at the top of the queue (the item that was 'first in')
    # and decrement the size of the queue by one.
    # This can be done by calling the remove_from_head method in our DLL. 
    def dequeue(self):
        # if the queue is empty just return from function
        if self.size < 1:
            return 
        # else decrement size of queue by one and return value of DLL remove_from_head method    
        else:    
            self.size -= 1
            return self.storage.remove_from_head() 

    # return value of queue's 'size' attr
    def len(self):
        return self.size
