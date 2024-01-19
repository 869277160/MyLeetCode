#
# @lc app=leetcode.cn id=404 lang=python3
#
# [404] 左叶子之和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        if root == None:
            return 0
        
        if root.left == None and root.right == None:
            return 0
        
        if root.left != None and root.right == None:
            if root.left.left == None and root.left.right == None:
                return root.left.val
            else :
                return self.sumOfLeftLeaves(root.left)

        if root.left == None and root.right != None:
            return self.sumOfLeftLeaves(root.right)
        
        if root.left != None and root.right != None:
            if root.left.left == None and root.left.right == None:
                return root.left.val + self.sumOfLeftLeaves(root.right)
            else :
                return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)

      
        
# @lc code=end

