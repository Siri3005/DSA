# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        result=[]
        def helper(root,result):
            if not root:
                return
            helper(root.left,result)
            helper(root.right,result)
            result.append(root.val)
            return result
        helper(root,result)
        return result
