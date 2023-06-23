# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # base case: check if the root is Null
        if root is None:
            return None
        
        # swap the positions of the children of each Node
        root.right, root.left = root.left, root.right
        
        # invert every right and left subtree 
        self.invertTree(root.right)
        self.invertTree(root.left)
        
        return root
        