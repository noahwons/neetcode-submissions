class ListNode:
    def __init__(self, key, next=None):
        self.key = key
        self.next = next

class MyHashMap:

    def __init__(self):
        self.hashMap = [ListNode(0) for i in range(10**4)]

    def put(self, key: int, value: int) -> None:
        cur = self.hashMap[self.hash_function(key)]
        cur.val = key
        if not cur.next:
            cur.next = ListNode(value)
            return
        cur.next.key = value

    def get(self, key: int) -> int:
        cur = self.hashMap[self.hash_function(key)]
        if cur.next:
            return cur.next.key
        return -1

    def remove(self, key: int) -> None:
        cur = self.hashMap[self.hash_function(key)]
        cur.next = None
        cur.val = 0

    def hash_function(self, key):
        return key % len(self.hashMap)
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)