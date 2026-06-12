class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c : set() for w in words for c in w}

        # go through all pairs
        # len(words) - 1 because we want to grab
        # next word for each iteration
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))
            # check that prefix is the same
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                # invalid
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    # break because we want first differing char
                    adj[w1[j]].add(w2[j])
                    break

        visit = {} # False=visited, True=visited, & in current path
        res = []

        def dfs(c):
            if c in visit:
                # if this returns true, a node has been found in current path twice
                # this will indicate a loop if it returns true
                return visit[c]
            
            visit[c] = True # indicate visited and in current path

            for nei in adj[c]:
                if dfs(nei):
                    return True


            visit[c] = False # indicate it has been visited but is no longer in the current path

            # post order, this is when we append
            # remember it gets returned in reverse order
            res.append(c)

        for c in adj:
            if dfs(c):
                # loop detected
                return ""

        # reverse b/c it was created in reverse order
        res.reverse()
        return "".join(res)




