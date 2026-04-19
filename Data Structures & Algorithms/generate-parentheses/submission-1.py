class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []
        o_count = n
        c_count = n
        brackets = ["("]
        self.helper(brackets, output, o_count - 1, c_count)
        return output
    
    def helper(self, brackets, output, o_count, c_count):
        print(brackets)
        if o_count == 0 and c_count == 0:
            print(brackets)
            output.append("".join(brackets))
            return
        if o_count > 0:
            brackets.append("(")
            self.helper(brackets, output, o_count - 1, c_count)
            brackets.pop()
        if c_count > 0 and c_count > o_count:
            brackets.append(")")
            self.helper(brackets, output, o_count, c_count - 1)
            brackets.pop()
        return

"""
2^n + 2^n
2(2)
"""