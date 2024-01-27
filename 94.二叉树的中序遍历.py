'''
Author: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
Date: 2023-02-08 09:40:50
LastEditors: DingWang wangding19@mails.ucas.ac.cn
LastEditTime: 2024-01-19 16:09:56
FilePath: \Leetcode_Solver\94.二叉树的中序遍历.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # (1) 中序遍历是左中右
        
        # 结果返回
        self.res = [] 
        
        # 结束条件 
        if root == None:
            return []
        if root.left == None and root.right == None:
            return [root.val] 

        # 遍历
        self.traverse(root)
    
        return self.res 
    
    def traverse(self, root: Optional[TreeNode]):
        if root == None:
            return 
        
        self.traverse(root.left)
        self.res.append(root.val)
        self.traverse(root.right)
        
    
# @lc code=end

