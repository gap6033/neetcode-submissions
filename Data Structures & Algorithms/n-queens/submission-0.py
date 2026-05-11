class Solution:
    def __init__(self):
        self.output = []

    def solveNQueens(self, n: int) -> List[List[str]]:
        rows_to_col = {}
        positive_diagonal = set()
        negative_diagonal = set()
        cols = set()
        curr_row = 0
        for c in range(n):
            rows_to_col[curr_row] = c
            cols.add(c)
            positive_diagonal.add((curr_row + c))
            negative_diagonal.add((curr_row - c))
            self.helper(curr_row + 1, n, positive_diagonal, negative_diagonal, rows_to_col, cols)
            del rows_to_col[curr_row]
            cols.remove(c)
            positive_diagonal.remove((curr_row + c))
            negative_diagonal.remove((curr_row - c))
        return self.output

    def helper(self, curr_row, n, positive_diagonal, negative_diagonal, rows_to_col, cols):
        if curr_row == n:
            self.output.append(self.build_board(rows_to_col, n))
            return
        for c in range(n):
            if c in cols:
                continue
            if (curr_row + c) in positive_diagonal or (curr_row - c) in negative_diagonal:
                continue
            rows_to_col[curr_row] = c
            cols.add(c)
            positive_diagonal.add((curr_row + c))
            negative_diagonal.add((curr_row - c))
            self.helper(curr_row + 1, n, positive_diagonal, negative_diagonal, rows_to_col, cols)
            del rows_to_col[curr_row]
            cols.remove(c)
            positive_diagonal.remove((curr_row + c))
            negative_diagonal.remove((curr_row - c))   

    def build_board(self, rows_to_col, n):
        board = []
        for r in range(n):
            curr_level = []
            for c in range(n):
                if rows_to_col[r] == c:
                    curr_level.append('Q')
                else:
                    curr_level.append('.')
            board.append(''.join(curr_level))
        return board
            

    

'''

'''