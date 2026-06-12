class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort intervals based on start time
        intervals.sort(key=lambda x: x[0])

        # we have an overlap when our current start time is between start and end of prev\
        res = [intervals[0]]
        # l, r = 0, 1
        # while r < len(start):
        #     if start[r][0] <= start[l][1]:
        #         res.append([start[l][0], max(start[r][1], start[l][1])])
        #         # update right in start to new cords
        #         start[r][0] = start[l][0]
        #         start[r][1] = start[l][1]
        #     else:
        #         res.append(start[l])
        #         l += 1
        #         r += 1

        if len(intervals) == 1:
            return intervals
        
        for start, end in intervals[1:]:
            if start <= res[-1][1]:
                res[-1][1] = max(res[-1][1], end)
            else:
                res.append([start, end])
        
        return res