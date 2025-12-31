# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        # 1. If both nodes are None, we've reached the end of both branches simultaneously.
        # They are identical at this position.
        if not p and not q:
            return True
        
        # 2. If one node is None but the other isn't, OR if the values don't match,
        # the trees are not the same.
        if not p or not q or p.val != q.val:
            return False
        
        # 3. Recursively check the left children and the right children.
        # Both must return True for the trees to be considered the same.
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)