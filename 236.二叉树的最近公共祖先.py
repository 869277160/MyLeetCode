'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-25 21:52:52
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-25 21:53:47
FilePath: \Leetcode_Solver\236.二叉树的最近公共祖先.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=236 lang=python3
#
# [236] 二叉树的最近公共祖先
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode': 
        
        
        if root == None :
            return None 
        else :
            if root == p or root == q :
                return root 
        
        left = self.lowestCommonAncestor(root.left , p , q)
        right = self.lowestCommonAncestor(root.right , p , q)
        
        if left != None and right != None :
            return root
        if left != None and right == None :
            return left 
        if left == None and right != None :
            return right 
        if left == None and right == None :
            return None 

        
        
        
# @lc code=end

