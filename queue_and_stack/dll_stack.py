import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    # Because stacks operate according to Last In First Out ordering, 
    # the push method will add the item to the top of the stack and increment the size of the stack by one.
    # Like a stack of plates in real life, when you add a plate to the stack, you add it to the top.
    # This can be done by calling the add_to_head method in our DLL class, passing in the value we want to add.
    def push(self, value):
        self.storage.add_to_head(value)
        self.size += 1

    # The pop method will remove the item at the top of the stack (the item that was 'last in')
    # and decrement the size of the stack by one.
    # If you had a stack of plates in real life and wanted to remove one, you'd probably remove it from the top of the stack.
    # This can be done by calling the remove_from_head method in our DLL. 
    def pop(self):
        # If the size of the stack is less than one just return from function 
        if self.size < 1:
            return
        # else decrement size of stack by one and remove the first item in the stack by calling the remove_from_head function
        # in our DLL class
        else:
            self.size -= 1
            return self.storage.remove_from_head()

    def len(self):
        return self.size
