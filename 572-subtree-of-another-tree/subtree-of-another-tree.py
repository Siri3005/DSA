# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        if not subRoot:
            return True
        if not root:
            return False
        if self.helper(root,subRoot):
            return True
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
    
    def helper(self,s,q):
        if not s and not q:
            return True
        if s and not q:
            return False
        if not s and q:
            return False
        if s.val!=q.val:
            return False
        return self.helper(s.left,q.left) and self.helper(s.right,q.right)
        