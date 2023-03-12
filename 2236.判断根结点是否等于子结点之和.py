'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-17 09:32:40
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-17 09:33:24
FilePath: \Leetcode_Solver\2236.判断根结点是否等于子结点之和.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2236 lang=python3
#
# [2236] 判断根结点是否等于子结点之和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        
        if root is None:
            return True
        if root.left is None and root.right is None:
            return True
        if root.left is None:
            return root.val == root.right.val 
        if root.right is None:
            return root.val == root.left.val 
        if root.left is not None and root.right is not None:
            return root.val == root.left.val + root.right.val

