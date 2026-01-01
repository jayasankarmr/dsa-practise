# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        
        # We use a helper function to compare the two mirror sides
        return self.isMirror(root.left, root.right)

    def isMirror(self, left, right):
        # Base Case: Both sides are empty
        if not left and not right:
            return True
        
        # Base Case: One side is empty, or values don't match
        if not left or not right or left.val != right.val:
            return False
        
        # Recursive Step: 
        # Compare Left's Left with Right's Right AND
        # Compare Left's Right with Right's Left
        return self.isMirror(left.left, right.right) and self.isMirror(left.right, right.left)