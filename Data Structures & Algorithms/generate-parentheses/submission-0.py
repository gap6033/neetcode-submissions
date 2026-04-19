class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []
        o_count = n
        c_count = n
        self.helper("(", output, o_count - 1, c_count)
        return output
    
    def helper(self, brackets, output, o_count, c_count):
        if o_count == 0 and c_count == 0:
            output.append(brackets)
            return
        if o_count > 0:
            self.helper(brackets + "(", output, o_count - 1, c_count)
        if c_count > 0 and c_count > o_count:
            self.helper(brackets + ")", output, o_count, c_count - 1)
        return

"""
(()
"""