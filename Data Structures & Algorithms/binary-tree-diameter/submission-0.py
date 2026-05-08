# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.max_diameter = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left_diameter = self.diameter(root.left)
        right_diameter = self.diameter(root.right)
        curr_diameter = left_diameter + right_diameter
        self.max_diameter = max(self.max_diameter, curr_diameter)
        return self.max_diameter

    def diameter(self, root):
        if not root:
            return 0
        left_diameter = self.diameter(root.left)
        right_diameter = self.diameter(root.right)
        curr_diameter = left_diameter + right_diameter
        self.max_diameter = max(self.max_diameter, curr_diameter)
        return 1 + max(left_diameter, right_diameter)
