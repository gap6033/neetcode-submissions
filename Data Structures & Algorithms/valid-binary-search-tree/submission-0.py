# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        left_check = self.traverse(float('-inf'), root.val, root.left)
        right_check = self.traverse(root.val, float('inf'), root.right)
        return left_check and right_check

    def traverse(self, min_limit, max_limit, node):
        if not node:
            return True
        if node.val <= min_limit or node.val >= max_limit:
            return False
        left_check = self.traverse(min_limit, node.val, node.left)
        right_check = self.traverse(node.val, max_limit, node.right)
        return left_check and right_check
        