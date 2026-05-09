# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        root_index = [0]
        root = preorder[root_index[0]]
        limit = inorder.index(root)
        curr_node = TreeNode(root)
        root_index[0] += 1
        curr_node.left = self.traverse(curr_node, root_index, inorder, preorder, 0, limit)
        curr_node.right = self.traverse(curr_node, root_index, inorder, preorder, limit + 1, len(preorder))
        return curr_node

    def traverse(self, curr_node, root_index, inorder, preorder, left_limit, right_limit):
        if left_limit >= right_limit:
            return
        root = preorder[root_index[0]]
        limit = inorder.index(root)
        curr_node = TreeNode(root)
        root_index[0] += 1
        curr_node.left = self.traverse(curr_node, root_index, inorder, preorder, left_limit, limit)
        curr_node.right = self.traverse(curr_node, root_index, inorder, preorder, limit + 1, right_limit)
        return curr_node

'''
preorder = [1,2,3,4]
inorder = [4,3,2,1]

1

'''