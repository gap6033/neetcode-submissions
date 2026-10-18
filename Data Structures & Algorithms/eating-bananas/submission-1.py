class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        while l <= r:
            m = l + (r - l)//2
            if self.is_valid(m, piles, h):
                k = m
                r = m - 1
            else:
                l = m + 1
        return k
    
    def is_valid(self, rate, piles, time_limit):
        time_spent = 0
        for p in piles:
            time_spent += p // rate
            if p % rate != 0:
                time_spent += 1
            if time_spent > time_limit:
                return False
        return True

'''
min = min(piles)
max = max(piles)
'''