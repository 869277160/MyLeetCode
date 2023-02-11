'''
Author: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
Date: 2023-02-11 10:07:52
LastEditors: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
LastEditTime: 2023-02-11 10:14:02
FilePath: \Leetcode_Solver\671.二叉树中第二小的节点.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=671 lang=python3
#
# [671] 二叉树中第二小的节点
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        if root == None: return -1
        if root.left == None and root.right == None: return -1
        
        min,sec_min = self.find(root, root.val,)
        
        
        
    def Helper(self, root, min,sec_min):
        
        
        return min
        
        
        
# @lc code=end

