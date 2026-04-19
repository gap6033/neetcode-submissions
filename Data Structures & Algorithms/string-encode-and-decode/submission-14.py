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
            j = i
            while s[j] != '#':
                j += 1

            length = int(s[i:j])
            i = j + 1

            output.append(s[i:i + length])
            i += length
        return output
        

'''
[#1313r5353r5, 1345135r545]

12##1313r5353r5
'''
