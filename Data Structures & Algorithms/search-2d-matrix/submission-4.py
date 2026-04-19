class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r = self.find_row(matrix, target)
        if r == -1:
            return False
        row = matrix[r]
        return self.search_row(row, target)

    def find_row(self, matrix, target):
        l = 0
        r = len(matrix) - 1
        while l <= r:
            m = l + (r - l)//2
            if target >= matrix[m][0] and target <= matrix[m][-1]:
                return m
            elif matrix[m][-1] < target:
                l = m + 1
            elif matrix[m][-1] > target:
                r = m - 1
        return -1

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