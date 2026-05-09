# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        preorder = []
        self.preorder(root, preorder)
        return ','.join(preorder)


    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        preorder = data.split(',')
        i = [0]
        if preorder[i[0]] == 'N':
            i[0] += 1
            return None
        node = TreeNode(int(preorder[i[0]]))
        i[0] += 1
        node.left = self.traverse(preorder, i)
        node.right = self.traverse(preorder, i)
        return node

    def traverse(self, preorder, i):
        if preorder[i[0]] == 'N':
            i[0] += 1
            return None
        node = TreeNode(int(preorder[i[0]]))
        i[0] += 1
        node.left = self.traverse(preorder, i)
        node.right = self.traverse(preorder, i)
        return node


    def preorder(self, root, output):
        if not root:
            output.append('N')
            return
        output.append(str(root.val))
        self.preorder(root.left, output)
        self.preorder(root.right, output)
        
