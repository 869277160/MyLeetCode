'''
Author: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
Date: 2023-02-10 23:21:00
LastEditors: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
LastEditTime: 2023-02-10 23:28:27
FilePath: \Leetcode_Solver\2331.计算布尔二叉树的值.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2331 lang=python3
#
# [2331] 计算布尔二叉树的值
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
      
        if root.val == 0 : 
            return False 
        if root.val == 1 : 
            return True 
        if root.val == 2:
            return self.evaluateTree(root.left) or self.evaluateTree(root.right)
        if root.val == 3:
            return self.evaluateTree(root.left) and self.evaluateTree(root.right)
        
        
        
        
        
        
        
        
        
# @lc code=end

