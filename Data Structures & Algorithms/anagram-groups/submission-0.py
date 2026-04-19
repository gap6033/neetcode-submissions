class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_map = {}
        for s in strs:
            freq_count = [0] * 26
            for i in range(len(s)):
                freq_count[ord(s[i]) - ord('a')] += 1
            freq_count = tuple(freq_count)
            if freq_count not in word_map:
                word_map[freq_count] = []
            word_map[freq_count].append(s)
        output = []
        for key in word_map:
            anagrams = word_map[key]
            output.append(anagrams)
        return output
            

        
'''
[]
[]
[]
[]
[]
n
'''            