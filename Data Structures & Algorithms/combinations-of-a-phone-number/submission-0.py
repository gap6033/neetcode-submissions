class Solution:
    def __init__(self):
        self.output = []

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        digitToChar = {
                    "2": "abc",
                    "3": "def",
                    "4": "ghi",
                    "5": "jkl",
                    "6": "mno",
                    "7": "qprs",
                    "8": "tuv",
                    "9": "wxyz",
                }
        curr_seq = []
        curr_index = 0
        for char in digitToChar[digits[curr_index]]:
            curr_seq.append(char)
            self.helper(curr_index + 1, curr_seq, digits, digitToChar)
            curr_seq.pop()
        return self.output

    def helper(self, curr_index, curr_seq, digits, digitToChar):
        if curr_index == len(digits):
            self.output.append(''.join(curr_seq))
            return
        for char in digitToChar[digits[curr_index]]:
            curr_seq.append(char)
            self.helper(curr_index + 1, curr_seq, digits, digitToChar)
            curr_seq.pop()

