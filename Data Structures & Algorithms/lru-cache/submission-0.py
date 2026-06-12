class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {} # Maps key to node
        self.cap = capacity

        self.left, self.right = Node(0,0), Node(0,0)
        # Left Node      Right Node
        #        ---------->
        #        <----------
        
        # left = LRU, right=most recent
        self.left.next, self.right.prev = self.right, self.left
    
    # remove from linked list
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    # insert node at right
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            # Update to most recent
            # Remove and reinsert at rightmost position
            self.remove(self.cache[key])
            self.insert(self.cache[key])

            # Keys are pointing to a node
            return self.cache[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Node already exists, we have to remove
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value) 
        
        # insert into linked list
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            # remove from list and delete LRU from cache (hashmap)
            # our left pointer tells us what the lru is
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

