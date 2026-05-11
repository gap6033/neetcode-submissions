class Solution:
    def __init__(self):
        self.output = []

    def partition(self, s: str) -> List[List[str]]:

        
        curr_str = ''
        curr_seq = []
        for j in range(len(s)):
            curr_str += s[j]
            if self.valid_palindrome(curr_str):
                curr_seq.append(curr_str)
                self.helper(curr_seq, j + 1, s)
                curr_seq.pop()
        return self.output


    def helper(self, curr_seq, curr_index, s):
        if curr_index == len(s):
            self.output.append(curr_seq.copy())
            return
        
        curr_str = ''
        for j in range(curr_index, len(s)):
            curr_str += s[j]
            if self.valid_palindrome(curr_str):
                curr_seq.append(curr_str)
                self.helper(curr_seq, j + 1, s)
                curr_seq.pop()

    def valid_palindrome(self, word):
        l = 0
        r = len(word) - 1
        while l < r:
            if word[l] != word[r]:
                return False
            r -= 1
            l += 1
        return True


                            