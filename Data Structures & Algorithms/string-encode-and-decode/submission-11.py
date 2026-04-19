class Solution:

    def encode(self, strs: List[str]) -> str:
        output = []
        for s in strs:
            output.append(str(len(s)) + '#' + s) 
        return ''.join(output)

    def decode(self, s: str) -> List[str]:
        output = []
        i = 0
        while i < len(s):
            length = ''
            while s[i] != '#':
                length += s[i]
                i += 1
            i += 1
            curr_str = ''
            for j in range(i, i + int(length)):
                curr_str += s[j]
            output.append(curr_str)
            i = i + int(length)
        return output
        

'''
[#1313r5353r5, 1345135r545]

12##1313r5353r5
'''
