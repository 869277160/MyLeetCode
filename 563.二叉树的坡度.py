'''
Author: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
Date: 2023-02-10 23:06:34
LastEditors: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
LastEditTime: 2023-02-10 23:20:25
FilePath: \Leetcode_Solver\563.二叉树的坡度.py
Description:

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=563 lang=python3
#
# [563] 二叉树的坡度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        
    #     if root == None : 
    #         return 0
        
    #     if root.left == None and root.right == None: 
    #         return 0
    #     if root.left != None and root.right == None: 
    #         return max(self.findTilt(root.left),0) - min(self.findTilt(root.left),0)
    #     if root.left == None and root.right != None: 
    #         return max(0,self.findTilt(root.right)) - min(0,self.findTilt(root.right))
    #     if root.left != None and root.right != None: 
    #         return max(self.findTilt(root.left),self.findTilt(root.right)) - min(self.findTilt(root.left),self.findTilt(root.right))
        
    # def Helper(self, root, res):
    #     if root == None:
    #         return 0
    #     if self.isLeef(root.left) and self.isLeef(root.right):
    #         return max(root.left.val,root.right.val) - min(root.left.val,root.right.val)
    #     if self.isLeef(root.left) and self.isLeef(root.right):
    #         return root.val + self.Helper(root.left,res)
    #     if self.isLeef(root.left) and self.isLeef(root.right):
    #         return root.val + self.Helper(root.right,res)
    #     if not self.isLeef(root.left) and not self.isLeef(root.right):
    #         return root.val + self.Helper(root.left,res) + self.Helper(root.right,res)
        
    # def isLeef(self, root):
    #     if root == None:
    #         return False
    #     if root.left == None and root.right == None:
    #         return True
    #     return False
        
        
        
# @lc code=end

