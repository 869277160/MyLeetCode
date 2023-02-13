'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-12 16:27:32
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-12 16:34:45
FilePath: \Leetcode_Solver\958.二叉树的完全性检验.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=958 lang=python3
#
# [958] 二叉树的完全性检验
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if root == None :
            return False 
        if root.left == None and root.right == None :
            return True 
        if root.left != None and root.right == None and root.left.left == None and root.left.right == None :
            return True 
        
        return self.isCompleteTreeHelper(root)    
        
    def isCompleteTreeHelper(self, root: Optional[TreeNode]) -> bool:
        if root.left == None and root.right == None :
            return False 
        if root.left == None and root.right != None :
            return False 
        if root.left != None and root.right == None :
            if root.left.left == None and root.left.right == None and root.right == None:
                return True
            else :
                return False 
        if root.left != None and root.right != None :
            if root.left.left == None and root.left.right == None and root.right.left == None and root.right.right == None:
                return True
            else :
                return self.isCompleteTreeHelper(root.left) and self.isCompleteTreeHelper(root.right)
        
      
        
# @lc code=end

