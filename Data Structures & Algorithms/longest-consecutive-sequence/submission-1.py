class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set()
        for num in nums:
            nums_set.add(num)
        
        max_count = 0
        for num in nums:
            if num in nums_set:
                nums_set.remove(num)
            else:
                continue
            less_than = self._check_less(num - 1, nums_set)
            greater_than = self._check_greater(num + 1, nums_set)
            total = less_than + greater_than + 1
            max_count = max(total, max_count)
        return max_count


    def _check_less(self, num, nums_set):
        if num not in nums_set:
            return 0
        ans = 0
        while num in nums_set:
            ans += 1
            nums_set.remove(num)
            num -= 1
        return ans

    def _check_greater(self, num, nums_set):
        if num not in nums_set:
            return 0
        ans = 0
        while num in nums_set:
            ans += 1
            nums_set.remove(num)
            num += 1
        return ans
            
            

