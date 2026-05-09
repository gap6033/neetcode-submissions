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
        left_children_index_limit = inorder.index(root)
        left_children = inorder[:left_children_index_limit]
        right_children = inorder[left_children_index_limit + 1:]
        curr_node = TreeNode(root)
        root_index[0] += 1
        if left_children:
            curr_node.left = self.traverse(curr_node, root_index, left_children, preorder)
        if right_children:
            curr_node.right = self.traverse(curr_node, root_index, right_children, preorder)
        return curr_node

    def traverse(self, curr_node, root_index, inorder, preorder):
        root = preorder[root_index[0]]
        left_children_index_limit = inorder.index(root)
        left_children = inorder[:left_children_index_limit]
        right_children = inorder[left_children_index_limit + 1:]
        curr_node = TreeNode(root)
        root_index[0] += 1
        if left_children:
            curr_node.left = self.traverse(curr_node, root_index, left_children, preorder)
        if right_children:
            curr_node.right = self.traverse(curr_node, root_index, right_children, preorder)
        return curr_node


'''
preorder = [1,2,3,4]
inorder = [4,3,2,1]

1

'''