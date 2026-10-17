from collections import deque

class MinStack:

    def __init__(self):
        self.stack = []
        self.min_index = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min_index:
            if val < self.stack[self.min_index[-1]]:
                self.min_index.append(len(self.stack) - 1)
        else:
            self.min_index.append(len(self.stack) - 1)


    def pop(self) -> None:
        if self.min_index[-1] == len(self.stack) - 1:
            self.min_index.pop()
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.stack[self.min_index[-1]]

'''
7, 9, 8, 4

stack = [7, 9, 4]
min_stack = [0, 3]

'''
        
