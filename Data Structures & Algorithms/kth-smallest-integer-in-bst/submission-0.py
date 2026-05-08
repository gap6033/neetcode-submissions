# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        output = []
        self.traverse(root.left, output)
        output.append(root)
        self.traverse(root.right, output)

        return output[k - 1].val


    def traverse(self, root, output):
        if not root:
            return
        self.traverse(root.left, output)
        output.append(root)
        self.traverse(root.right, output)