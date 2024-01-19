'''
Author: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
Date: 2023-02-10 22:39:37
LastEditors: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
LastEditTime: 2023-02-10 22:50:36
FilePath: \Leetcode_Solver\965.单值二叉树.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=965 lang=python3
#
# [965] 单值二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        # 结束条件
        if root == None : return True
        
        # 四种情况单独判断
        if root.left == None and root.right == None: 
            return True
        if root.left == None and root.right != None:
            input1 = self.isUnivalTree(root.left) and self.isUnivalTree(root.right)
            input2 = True
            input3 = root.val == root.right.val

            return input1 and input2 and input3
        if root.left != None and root .right == None:
            input1 = self.isUnivalTree(root.left) and self.isUnivalTree(root.right)
            input2 = root.val == root.left.val 
            input3 = True 

            return input1 and input2 and input3
        
        if root.left != None and root .right != None:
            # 判断左右子树是否为单值树
            input1 = self.isUnivalTree(root.left) and self.isUnivalTree(root.right)
            input2 = root.val == root.left.val 
            input3 = root.val == root.right.val

            return input1 and input2 and input3
        
# @lc code=end

