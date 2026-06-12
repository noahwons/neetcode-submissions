class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Each task 1 unit time
        # minimize idle times

        # O(n * m) where m represents idle time
        # O(n) operation because heapify runs in log(26)

        count = Counter(tasks)

        # create array with - count of each task
        maxHeap = [-cnt for cnt in count.values() ]
        heapq.heapify(maxHeap)

        time = 0
        q = deque() # paris of [-cnt, idleTime]

        while maxHeap or q:
            time += 1

            if maxHeap:
                # add one because values are negative
                cnt = 1 + heapq.heappop(maxHeap)
                # when we pop it means we are processing
                if cnt:
                    # time + n is when this task is available
                    q.append([cnt, time + n])
            
            if q and q[0][1] == time:
                # idle time has been reached for first task in q
                # add first value in q to heap
                heapq.heappush(maxHeap, q.popleft()[0])

        return time