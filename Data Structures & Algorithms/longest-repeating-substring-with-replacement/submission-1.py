class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq_array = [0] * 26
        l = 0
        r = 0
        max_len = 0
        while r < len(s):
            # print('r', r, ord(s[r].lower()) - ord('a'))
            freq_array[ord(s[r].lower()) - ord('a')] += 1
            max_freq = self.get_max_freq(freq_array)
            if self.sequence_valid(l, r, max_freq, k):
                max_len = max(r - l + 1, max_len)
            else:
                while not self.sequence_valid(l, r, max_freq, k):
                    freq_array[ord(s[l].lower()) - ord('a')] -= 1
                    max_freq = self.get_max_freq(freq_array)
                    l += 1
            r += 1
        return max_len

    def get_max_freq(self, freq_array):
        max_val = 0
        for i in range(len(freq_array)):
            if freq_array[i] > max_val:
                max_val = freq_array[i] 
        return max_val
    

    def sequence_valid(self, l, r, max_freq, k):
        if r - l + 1 - max_freq <= k:
            return True
        return False

'''
ABBBBBA
l = 0
r = 0

'''