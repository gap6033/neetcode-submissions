class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r = self.find_row(matrix, target)
        if r > len(matrix) - 1:
            return False
        row = matrix[r]
        return self.search_row(row, target)

    def find_row(self, matrix, target):
        l = 0
        r = len(matrix) - 1
        while l < r:
            m = l + (r - l)//2
            if matrix[m][-1] < target:
                l = m + 1
            elif matrix[m][-1] > target:
                r = m - 1
            else:
                return m
        if matrix[r][-1] < target:
            return r + 1
        return r

    def search_row(self, row, target):
        l = 0
        r = len(row) - 1
        while l <= r:
            m = l + (r - l)//2
            if row[m] < target:
                l = m + 1
            elif row[m] > target:
                r = m - 1
            else:
                return True
        return False
        


