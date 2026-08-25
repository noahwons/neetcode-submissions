class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # if the start of the new interval is less than or equal to the end the current
        # they should merge

        res = []

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                # no more overlapping, add rest
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                # current interval goes before newInterval
                res.append(intervals[i])
            else:
                # newInterval is overlapping
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        
        res.append(newInterval)
                
        return res