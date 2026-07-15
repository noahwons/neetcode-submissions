class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        p = 0
        added = False

        while p < len(intervals):
            while p < len(intervals) and intervals[p][1] < newInterval[0]:
                # goes before, append
                res.append(intervals[p])
                p+=1

            if p >= len(intervals):
                res.append(newInterval)
                return res
                
            if intervals[p][0] > newInterval[1]and not added:
                # goes before
                res.append(newInterval)
                res.append(intervals[p])
                added = True
            elif added and intervals[p][0] > newInterval[1]:
                res.append(intervals[p])
            else:
                # update newInterval
                newInterval = [min(intervals[p][0], newInterval[0]), max(intervals[p][1], newInterval[1])]

            p += 1

        if not res:
            res.append(newInterval)
            return res

        return res