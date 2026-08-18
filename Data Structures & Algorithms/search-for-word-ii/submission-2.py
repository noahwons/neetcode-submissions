class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS, COLS = len(board), len(board[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        root = TrieNode()
        res, path = set(), set()
        
        for w in words:
            cur = root
            for c in w:
                if c not in cur.children:
                    cur.children[c] = TrieNode()
                cur = cur.children[c]
            cur.word = True

        
        def dfs(r, c, cur, word):
            if (r, c) in path or r not in range(ROWS) or c not in range(COLS) or board[r][c] not in cur.children:
                return 
            
            word += board[r][c]
            cur = cur.children[board[r][c]]
            if cur.word:
                res.add(word)

            path.add((r, c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                dfs(nr, nc, cur, word)
                    
            path.remove((r, c))
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] in root.children:
                    dfs(r, c, root, '')
        
        return list(res)

            
