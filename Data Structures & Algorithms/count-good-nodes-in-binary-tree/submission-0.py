# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    good_count = 0

    def goodNodes(self, root: TreeNode) -> int:
        self.traverse(root, float('-inf'))
        return self.good_count

    def traverse(self, root, curr_max):
        if not root:
            return
        if root.val >= curr_max:
            self.good_count += 1
        self.traverse(root.left, max(curr_max, root.val))
        self.traverse(root.right, max(curr_max, root.val))