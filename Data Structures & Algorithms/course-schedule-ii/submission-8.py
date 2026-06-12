class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # we can convert prerequisites to graph using hashmap
        # run dfs, use 2 sets to keep track of cycle detection
        # and keep track of work already completed
        preMap = {i : [] for i in range(numCourses)}
        visit, cycle = set(), set()

        # use res to store valid path
        res = []

        def dfs(crs):
            # if crs is in cycle set, a cycle has been detected
            if crs in cycle:
                return False
            
            # if crs in visit, work is already completed
            if crs in visit:
                return True
            
            cycle.add(crs)

            # detect cycle
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            
            # we have validated current path
            visit.add(crs)
            res.append(crs)

            # no longer looking for cycle, reset for next itr
            cycle.remove(crs)
            return True


        # 1. populate preMap
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        for crs in range(numCourses):
            if not dfs(crs):
                # invalid, loop detected
                return []
        
        return res