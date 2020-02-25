from doubly_linked_list import DoublyLinkedList
class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.limit = limit
        self.current_size = 0
        self.entries = DoublyLinkedList()
        self.storage = dict()

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        if key not in self.storage:
            return None

        # move the node stored at the given key in our dictionary to the front (head) of the doubly linked list (making it the MOST recently accessed node)
        self.entries.move_to_front(self.storage[key])  
        # return the value of the node at the given key in our dictionary 
        # could also return self.entries.head.value since we have just moved the node to the front of our DLL 
        return self.storage[key].value

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        # if the key already exists in storage
        if key in self.storage:
            # move the node stored at the given key in storage to the front (head) of the doubly linked list (making it the MOST recently used node)
            self.entries.move_to_front(self.storage[key])  
            # overwrite the value the node contains with value passed into 'set' method 
            # (could also directly set value of head node in DLL equal to value passed into function, seeing as we've just moved the node to the head of the DLL)
            self.storage[key].value = value

        # if the cache is at max capacity (current_size is equal to the limit)
        elif self.current_size == self.limit:
           # remove the node at the tail of the DLL (this will be the Least recently used node), 
           # and save the value of the node we've just removed from the tail to variable
           removed_node = self.entries.remove_from_tail()
           # update storage to only hold key value pairs where the value of the node stored at any key is not equal to the value of the node we have just removed from the tail of the DLL
           self.storage = { k:v for k, v in self.storage.items() if v.value != removed_node }
           # add a new node to the head of the DLL containing the value we are passing into the 'set' function, making it the MOST recently used
           self.entries.add_to_head(value)
           # add new key value pair to storage where key = key and value = the node we've just added to the head of the DLL 
           self.storage[key] = self.entries.head

        # else the key must not already exist in storage AND we are not at max capacity
        else:
            # add a new node to the head of the DLL containing the value we are passing into the 'set' function, making it the MOST recently used
            self.entries.add_to_head(value)  
            # add new key value pair to storage where key = key and value = the node we've just added to the head of the DLL  
            self.storage[key] = self.entries.head
            # increment the current size of storage by one because we have just added a new key value pair
            self.current_size += 1

