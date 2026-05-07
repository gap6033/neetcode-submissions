from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        grid = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[r])):
                val = board[r][c]
                if val == ".":
                    continue
                if val in rows[r] or val in cols[c] or val in grid[(r//3, c//3)]:
                    return False
                rows[r].add(val)
                cols[c].add(val)
                grid[(r//3, c//3)].add(val)
        return True




"""

"""