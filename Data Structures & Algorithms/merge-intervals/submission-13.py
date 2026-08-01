class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # ex: [1, 3] and [1, 5] are overlapping
        # explanation: these intervals are overlapping because
        # [1, 5] occurs during interval [1, 3]

        # Note: It is not simply that the interval ends after or starts before,
        # it is overlapping because it occurs during

        # How can we identify all intervals that are overlapping?
        if len(intervals) == 1:
            return intervals
        
        if not intervals:
            return []

        # sort based on start position
        intervals.sort(key=lambda x: x[0])
        res = [intervals[0]]

        print(intervals)

        for i in range(1, len(intervals)):
            if intervals[i][0] <= res[-1][1]:
                print("overlapping")
                print(res)
                res[-1][1] = max(intervals[i][1], res[-1][1])
                print(res)
            else:
                res.append([intervals[i][0], intervals[i][1]])

        return res
