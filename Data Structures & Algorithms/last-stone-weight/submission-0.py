class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # create minheap by multiplying by -1
        stones = [-s for s in stones]
        heapq.heapify(stones) # O(n) operation

        while len(stones) > 1:
            # get two largest stones
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)

            # reverse the operation since all vals in minheap are negative
            if second > first:
                # second will have smaller or equal weight

                # get difference and push to heap
                heapq.heappush(stones, first - second)
        
        stones.append(0) # add 0 so stones is never empty
        return abs(stones[0])