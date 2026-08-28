class MedianFinder:
    # heapq.heappush_max(heap, item
    def __init__(self):
        self.left, self.right = [], [] # left = maxHeap, right = minHeap

    def addNum(self, num: int) -> None:
        heapq.heappush_max(self.left, num)
        if (len(self.left) - len(self.right)) > 1:
            # remove top left add to right
            val = heapq.heappop_max(self.left)
            heapq.heappush(self.right, val)
        if (len(self.right) - len(self.left)) > 1:
            # remove top right add to left
            val = heapq.heappop(self.right)
            heapq.heappush_max(self.right, val)
        # we have to ensure that all values in left < all values in right
        # if the max from the left > min from the right, we have to rebalance
        # we can rebalance by swapping the max left and min right
        if len(self.right) > 0 and len(self.left) > 0 and self.right[0] < self.left[0]:
            maxLeft = heapq.heappop_max(self.left)
            minRight = heapq.heappop(self.right)
            heapq.heappush_max(self.left, minRight)
            heapq.heappush(self.right, maxLeft)


    def findMedian(self) -> float:
        # if total len is odd, pop from left
        totalLen = len(self.left) + len(self.right)
        if totalLen % 2 != 0:
            return self.left[0]
        else:
            return (self.right[0] + self.left[0]) / 2
        