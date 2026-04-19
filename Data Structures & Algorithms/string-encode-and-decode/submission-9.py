class Solution:
    def __init__(self):
        self.random_str = '_134389_'

    def encode(self, strs: List[str]) -> str:
        output_str = ''
        for word in strs:
            output_str += str(len(word))+"#"+word
        print(output_str)
        return output_str

    def decode(self, s: str) -> List[str]:
        curr_index = 0
        output = []
        while curr_index < len(s):
            length = s[curr_index]
            curr_index += 1
            while s[curr_index] != "#":
                length += s[curr_index]
                curr_index += 1
            length = int(length)
            word_start = curr_index + 1
            word_end = word_start + length
            output.append(s[word_start: word_end]) 
            curr_index = word_end
        return output      

"""
4#sand
2
6
"""     
        

'''
4#neet4#code
'''
