# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        level = deque()
        level.append(root)
        levels = []
        while level:
            curr_level = []
            for i in range(len(level)):
                node = level.popleft()
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
                curr_level.append(node.val)
            levels.append(curr_level)
        return levels
