class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        next_greater = []
        lgi = []
        for i in range(len(temperatures) - 1, -1, -1):
            curr_temp = temperatures[i]
            while lgi and temperatures[lgi[-1]] <= curr_temp:
                lgi.pop()
            if lgi:
                next_greater.append(lgi[-1] - i)
            elif not lgi:
                next_greater.append(0)
            lgi.append(i)
        return next_greater[::-1]