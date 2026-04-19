class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        return self.get_next_greater(temperatures)[::-1]

    def get_next_greater(self, array):
        stack = []
        next_greater = []
        for i in range(len(array) - 1, -1, -1):
            while stack and array[stack[-1]] <= array[i]:
                stack.pop()
            if not stack:
                next_greater.append(0)
            else:
                next_greater.append(stack[-1] - i)
            stack.append(i)
        return next_greater
