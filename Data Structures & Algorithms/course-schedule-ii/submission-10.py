class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # build adjacency list of prereqs
        prereq = {c : [] for c in range(numCourses)}
        for crs, pre in prerequisites:
            prereq[crs].append(pre)
        
        # a course has 3 possible states

        # visited -> crs has been added to output
        # visiting -> crs not added to output but added to cycle
        # unvisited -> crs not added to output or cycle
        output = []
        visit, cycle = set(), set()

        def dfs(crs):
            if crs in cycle:
                return False

            if crs in visit:
                return True
            
            # add crs to cycle to find cycles
            cycle.add(crs)
            for pre in prereq[crs]:
                if not dfs(pre):
                    return False
            
            # indicate true
            visit.add(crs) # confirmed this course is valid
            output.append(crs)

            cycle.remove(crs) # crs no longer along path
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return []
        
        return output
