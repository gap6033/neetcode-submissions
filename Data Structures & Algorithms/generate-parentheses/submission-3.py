class Solution:
   
    def generateParenthesis(self, n: int) -> List[str]:
        open_count = n
        close_count = n
        output = []
        self.helper('(', open_count - 1, close_count, output)
        return output

    def helper(self, pattern, open_count, close_count, output):
        if open_count + close_count == 0:
            output.append(pattern)
            return
        
        if open_count > 0:
            self.helper(pattern + '(', open_count - 1, close_count, output)
        if open_count < close_count:
            self.helper(pattern + ')', open_count, close_count - 1, output)




    