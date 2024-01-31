#
# @lc app=leetcode.cn id=513 lang=python3
#
# [513] 找树左下角的值
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        
        if root == None:
            return root
        
        val, level = self.traverse(root, 0, root.val)
        
        return val 
        
        
    def traverse(self, root, level, res):
        if root == None:
            return res, level 
        
        left_res, left_level = -1, -1
        right_res, right_level = -1, -1
        if root.left != None:
            left_res, left_level = self.traverse(root.left, level+1, res)
        if root.right!= None:
            right_res, right_level = self.traverse(root.right, level+1, res)
        
        if left_level == -1 and right_level == -1:
            return root.val, level 
        elif left_level >= right_level:
            return left_res, left_level
        else:
            return right_res, right_level
        
# @lc code=end

