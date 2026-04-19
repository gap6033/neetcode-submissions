from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        blocks = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[r])):
                num = board[r][c]
                if num == ".":
                    continue
                if num in rows[r] or num in cols[c] or num in blocks[(r//3, c//3)]:
                    return False
                rows[r].add(num)
                cols[c].add(num)
                blocks[(r//3, c//3)].add(num)
        return True