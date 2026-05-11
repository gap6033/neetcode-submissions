
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        curr_index = 0
        for r in range(len(board)):
            for c in range(len(board[r])):
                char = board[r][c]
                if char == word[curr_index]:
                    visited.add((r, c))
                    for x, y in [(1, 0), (-1, 0), (0, 1), (0,-1)]:
                        new_r, new_c = r + x, c + y
                        if self.helper(word, 1, visited, new_r, new_c, board):
                            visited.remove((r,c))
                            return True
                    visited.remove((r,c))
        return False

    def helper(self, word, curr_index, visited, r, c, board):
        if curr_index == len(word):
            return True
        if r < 0 or r == len(board) or c < 0 or c == len(board[0]):
            return False
        if (r, c) in visited:
            return False
        if word[curr_index] == board[r][c]:
            visited.add((r, c))
            curr_index += 1
            for x, y in [(1, 0), (-1, 0), (0, 1), (0,-1)]:
                new_r, new_c = r + x, c + y
                if self.helper(word, curr_index, visited, new_r, new_c, board):
                    visited.remove((r,c))
                    return True
            visited.remove((r,c))
        return False

            
        



