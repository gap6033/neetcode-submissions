class Solution:
    def __init__(self):
        self.random_str = '_134389_'

    def encode(self, strs: List[str]) -> str:
        output_str = ''
        for word in strs:
            output_str += word+self.random_str
        return output_str

    def decode(self, s: str) -> List[str]:
        return s.split(self.random_str)[:-1]
        

'''
4#neet4#code
'''
