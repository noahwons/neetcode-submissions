class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # map each course to its prereq
        preMap = {i : [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        # visitSet = all courses along the current DFS path
        visitSet = set()
        def dfs(crs):
            if crs in visitSet:
                # visiting course twice, loop detected
                return False
            
            if preMap[crs] == []:
                # course has no prereqs thus it can be completed
                return True
            
            visitSet.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre): return False
                # can be taken

            visitSet.remove(crs)
            preMap[crs] = []
            return True
        
        for crs in range(numCourses):
            if not dfs(crs): return False
        return True
