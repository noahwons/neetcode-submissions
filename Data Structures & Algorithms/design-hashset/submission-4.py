class ListNode:
    def __init__(self, key, next=None):
        self.key = key
        self.next = next

class MyHashSet:

    def __init__(self):
        self.arr = [ListNode(0) for i in range(10**4)]

    def add(self, key: int) -> None:
        cur = self.arr[self.hash_function(key)]

        while cur.next:
            if cur.next.key == key:
                # duplicate found, return
                return
            cur = cur.next
        
        cur.next = ListNode(key)


    def remove(self, key: int) -> None:
        cur = self.arr[self.hash_function(key)]

        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next
        

    def contains(self, key: int) -> bool:
        cur = self.arr[self.hash_function(key)]

        while cur.next:
            if cur.next.key == key:
                return True
            cur = cur.next
        return False

    def hash_function(self, key):
        return key % len(self.arr)
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)