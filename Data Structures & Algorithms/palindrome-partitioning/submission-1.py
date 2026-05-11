class Solution:
    def __init__(self):
        self.output = []

    def partition(self, s: str) -> List[List[str]]:
        self.helper([], 0, s)
        return self.output


    def helper(self, curr_seq, curr_index, s):
        if curr_index == len(s):
            self.output.append(curr_seq.copy())
            return
        
        curr_str = ''
        for j in range(curr_index, len(s)):
            if self.valid_palindrome(s, curr_index, j):
                curr_seq.append(s[curr_index:j+1])
                self.helper(curr_seq, j + 1, s)
                curr_seq.pop()

    def valid_palindrome(self, word, l, r):
        while l < r:
            if word[l] != word[r]:
                return False
            r -= 1
            l += 1
        return True


                            