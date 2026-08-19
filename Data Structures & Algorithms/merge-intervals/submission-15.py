class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # if we sort based on the start values then we know the i + 1
        # interval must have >= start value
        # So if intervals are overlapping, it must be the case that
        # the i + 1 interval start is <= the end of i 

        # now that we have figured out how to determine overlap, how can we
        # build the result string?
        # we can use a tmp variable to keep track of the most recent interval
        # if it is the case that our current interval overlaps with that one,
        # we can simply update the values and update the variable
        if not intervals:
            return []

        intervals.sort(key=lambda x: x[0])
        res, tmp = [intervals[0]], intervals[0][1]

        # is the current value in the range of my tmp?
        #.   if so we merge then update
        # if not we add then update tmp
        for i in range(len(intervals)):
            if intervals[i][0] <= tmp:
                tmp = max(tmp, intervals[i][1])
                res[-1][1] = tmp

            else:
                res.append(intervals[i])
                tmp = intervals[i][1]

        
        return res
