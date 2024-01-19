#
# @lc app=leetcode.cn id=1339 lang=python3
#
# [1339] 分裂二叉树的最大乘积
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        
        
        def tree_sum(root):
            
            if root == None :
                return 0
            
            res = 0
            res += root.val
            if root.left:
                res += tree_sum(root.left)
            if root.right:
                res += tree_sum(root.right)
            
            return res 
            
            
        total = tree_sum(root)
            

        def root_last_travel(root):
            
            if root == None:
                return 0
            
            res = 0
            res += root.val
            if root.left:
                res += root_last_travel(root.left)
            if root.right:
                res += root_last_travel(root.right)
            
            return res - total
        
        
        
        
        
        
        
# @lc code=end

