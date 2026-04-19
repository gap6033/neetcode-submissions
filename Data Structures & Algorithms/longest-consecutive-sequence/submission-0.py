class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set()
        for num in nums:
            nums_set.add(num)

        max_sequence = 0
        for num in nums:
            if num in nums_set:
                nums_set.remove(num)
                l = self.check_less(num - 1, nums_set)
                r = self.check_greater(num + 1, nums_set)
                print(num, l, r)
                max_sequence = max(l + r + 1, max_sequence)
        return max_sequence
    
    def check_less(self, start, nums_set):
        count = 0
        while True:
            if start in nums_set:
                nums_set.remove(start)
                start -= 1
                count += 1
            else:
                break
        return count

    def check_greater(self, start, nums_set):
        count = 0
        while True:
            if start in nums_set:
                nums_set.remove(start)
                start += 1
                count += 1
            else:
                break
        return count
