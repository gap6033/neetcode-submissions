class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for word in strs:
            encoded_str += str(len(word))+"#" + word
        print(encoded_str)
        return encoded_str

    def decode(self, s: str) -> List[str]:
        output = []
        l = 0
        r = 0
        while r < len(s):
            curr_length = ""
            while s[l] != "#":
                curr_length += s[l]
                l += 1
            length = int(curr_length)
            r = l + 1
            curr_str = ""
            for i in range(r, r + length):
                curr_str += s[i]
            output.append(curr_str)
            l = r + length
            r = l
        return output
        

'''
4#neet4#code
'''
