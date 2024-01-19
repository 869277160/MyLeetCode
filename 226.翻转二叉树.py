'''
Author: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
Date: 2023-02-10 15:12:02
LastEditors: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
LastEditTime: 2023-02-10 22:38:17
FilePath: \Leetcode_Solver\226.翻转二叉树.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=226 lang=python3
#
# [226] 翻转二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # 如果没有叶子，则返回
        if root == None:
            return root 
        else:
            # 交换左右子树
            root.left,root.right = root.right,root.left
            # 递归调用
            self.invertTree(root.left)
            self.invertTree(root.right)
            return root
        
        
        
        
# @lc code=end

