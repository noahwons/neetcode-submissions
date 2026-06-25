class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.vals = nums
        self.k = k
        self.vals.sort(reverse=True)


    def add(self, val: int) -> int:
        self.vals.append(val)
        self.vals.sort(reverse=True)
        return self.vals[self.k-1]
        
