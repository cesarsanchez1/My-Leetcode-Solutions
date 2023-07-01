# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def isMirror(self, left, right):
        if left is None and right is None:
            return True
        if (left is None or right is None) or (left.val != right.val):
            return False
        return self.isMirror(left.left, right.right) and self.isMirror(left.right, right.left)
        
        
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return None
        
        return self.isMirror(root.left, root.right)
        
        