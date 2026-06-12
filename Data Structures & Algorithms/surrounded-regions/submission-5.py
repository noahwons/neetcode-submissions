class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        visit = set()

        def bfs(r, c):
            q = deque([(r, c)])
            visit.add((r, c))

            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (nr, nc) not in visit and nr in range(rows) and nc in range(cols) and board[nr][nc] == 'O':
                        visit.add((nr, nc))
                        q.append((nr, nc))

        for r in range(rows):
            for c in range(cols):
                if (r == 0 or c == 0 or r == rows - 1 or c == cols - 1) and board[r][c] == 'O':
                    bfs(r, c)
        
        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visit:
                    board[r][c] = 'X'