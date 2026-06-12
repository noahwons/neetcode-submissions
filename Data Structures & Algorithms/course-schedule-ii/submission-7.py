class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i : [] for i in range(numCourses)}
        # use the cycle set to determine cycle for each iteration
        # use visit set to determine if we are visiting a path we
        # have already visited.
        visit, cycle = set(), set()
        res = []
        
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        def dfs(crs):
            # run dfs on crs
            if crs in visit:
                # we return true here because this means we 
                # already traversed this path
                return True

            if crs in cycle:
                # loop detected
                return False
            
            cycle.add(crs)

            for pre in preMap[crs]:
                if not dfs(pre):
                    return False

            # valid path
            res.append(crs)
            cycle.remove(crs)
            visit.add(crs)
            return True

        
        for crs in range(numCourses):
            if not dfs(crs):
                return []

        return res

