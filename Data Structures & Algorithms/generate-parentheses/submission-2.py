class Solution:
    def __init__(self):
        self.output = []
    def generateParenthesis(self, n: int) -> List[str]:
        self.helper(['('], 1, 0, n)
        return self.output

    def helper(self, curr_seq, open_count, close_count, n):
        if open_count + close_count == 2*n:
            self.output.append(''.join(curr_seq))
            return
        if open_count < n:
            curr_seq.append('(')
            self.helper(curr_seq, open_count + 1, close_count, n)
            curr_seq.pop()
        if close_count < open_count:
            curr_seq.append(')')
            self.helper(curr_seq, open_count, close_count + 1, n)
            curr_seq.pop()



