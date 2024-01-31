'''
Author: DingWang wangding19@mails.ucas.ac.cn
Date: 2024-01-28 12:48:21
LastEditors: DingWang wangding19@mails.ucas.ac.cn
LastEditTime: 2024-01-28 13:07:32
FilePath: \Leetcode_Solver\530.二叉搜索树的最小绝对差.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=530 lang=python3
#
# [530] 二叉搜索树的最小绝对差
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        if root.left == None and root.right == None:
                return root.val
        
        _, current_res = self.traverse(root, [], -1)
        
        return current_res
    
    def traverse(self, root, res, current_res):
        if root == None:
            return res, current_res
        
        res, current_res = self.traverse(root.left, res, current_res)
        if res == []:
            res.append(root.val)
            res, current_res = self.traverse(root.right, res, current_res)
            return res, current_res
        else:
            if current_res == 0:
                return res, current_res
            else:
                result = max(root.val, res[-1]) - min(root.val, res[-1])
                current_res = min(current_res, result) if current_res != -1 else result
                res.append(root.val)
                res, current_res = self.traverse(root.right, res, current_res)
                return res, current_res
# @lc code=end

