class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res, sol = [], []
        n = len(candidates)

        candidates.sort() # sort so we skip duplicates
        def dfs(i, cur, total):
            # append cur if total is equal
            if total == target:
                res.append(sol[:])
                return
                
            # base case leaf node or target too large
            if i >= n or total > target:
                return
            
            # Decide to include or not

            # include
            # Do not include duplicates
            # since candidates is now sorted, we can skip over the current
            # element if it has a duplicate
            
            # include (dupes are considered here but we don't want to do it twice)
            # if we include dupes twice we end up with duplicate decision trees
            cur.append(candidates[i])
            dfs(i + 1, cur, total + candidates[i])

            # exclude
            cur.pop()
            # ensure that i + 1 is in bounds
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                # skip element all together to avoid dupes
                i += 1
            dfs(i + 1, cur, total)
        
        dfs(0, sol, 0)
        return res