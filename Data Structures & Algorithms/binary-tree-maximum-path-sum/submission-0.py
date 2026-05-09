# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    max_sum = float('-inf')
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        left_sum = self.traverse(root.left)
        right_sum = self.traverse(root.right)
        curr_max = max(root.val + left_sum, root.val + right_sum, root.val)
        self.max_sum = max(self.max_sum, curr_max, root.val + left_sum + right_sum)
        return self.max_sum

    def traverse(self, root):
        if not root:
            return 0
        left_sum = self.traverse(root.left)
        right_sum = self.traverse(root.right)
        curr_max = max(root.val + left_sum, root.val + right_sum, root.val)
        self.max_sum = max(self.max_sum, curr_max, root.val + left_sum + right_sum)
        return curr_max