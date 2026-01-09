
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        res = []
        self.helper(root, res)
        return res
    
    def helper(self, root, res):
        if root:
         
            self.helper(root.left, res)
            res.append(root.val)
            self.helper(root.right, res)