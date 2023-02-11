'''
Author: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
Date: 2023-02-10 22:56:15
LastEditors: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
LastEditTime: 2023-02-10 23:02:43
FilePath: \Leetcode_Solver\111.二叉树的最小深度.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root == None: 
            return 0
        else :
            if root.left == None and root.right == None : 
                return 1 
            if root.left == None and root.right != None : 
                return self.minDepth(root.right) + 1
            if root.left != None and root.right == None : 
                return self.minDepth(root.left) + 1
            if root.left != None and root.right != None : 
                return min(self.minDepth(root.left) + 1, self.minDepth(root.right) + 1)
        
# @lc code=end

