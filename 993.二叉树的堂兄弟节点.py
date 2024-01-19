'''
Author: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
Date: 2023-02-10 23:30:17
LastEditors: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
LastEditTime: 2023-02-10 23:45:22
FilePath: \Leetcode_Solver\993.二叉树的堂兄弟节点.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=993 lang=python3
#
# [993] 二叉树的堂兄弟节点
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        if root == None: return False 
        if root == x or root == y: return False
        if root.left == x and root.right == y: return False
        
        father_x, level_x = self.level(root.left, x,0)
        father_y, level_y = self.level(root.right,y,0)
        
        
        return (father_x != father_y) and (level_x == level_y)
        
        
    def level(self, root, x, level):
        
        if root.left == None and root.right == None:
            return None, level
        if root.left != None and root.right == None:
            return self.level(root.left, x, level+1)
        if root.left == None and root.right != None:
            return self.level(root.right, x, level+1)
        if root.left != None and root.right != None:
            father_x_l, level_x_l = self.level(root.left, x, level+1)
            father_x_r, level_x_r = self.level(root.right, x, level+1)
            if father_x_l == None :
                return father_x_r, level_x_r
            if father_x_r == None:
                return father_x_l, level_x_l

        
# @lc code=end

