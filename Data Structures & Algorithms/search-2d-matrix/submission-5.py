class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1

        while l <= r:
            m = l + (r - l)//2
            if target >= matrix[m][0] and target <= matrix[m][-1]:
                return self.find_target(matrix[m], target)
            elif target > matrix[m][-1]:
                l = m + 1
            elif target < matrix[m][-1]:
                r = m - 1
        return False

    def find_target(self, row, target):
        l = 0
        r = len(row)

        while l <= r:
            m = l + (r - l)//2
            if row[m] == target:
                return True
            elif row[m] < target:
                l = m + 1
            elif row[m] > target:
                r = m - 1
        return False



