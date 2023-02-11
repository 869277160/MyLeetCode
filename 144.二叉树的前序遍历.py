'''
Author: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
Date: 2023-02-08 09:53:29
LastEditors: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
LastEditTime: 2023-02-08 09:55:17
FilePath: \Leetcode_Solver\144.二叉树的前序遍历.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=144 lang=python3
#
# [144] 二叉树的前序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        # (1) 前序遍历是中左右
        # 
        
        # 结果返回
        res = []
        
        # 结束条件 
        if root == None:
            return []
        if root.left == None and root.right == None:
            return [root.val] 
        
        # 进一步搜索
        res += [root.val]
        res += self.preorderTraversal(root.left)
        res += self.preorderTraversal(root.right)

        return res 
    
        
        
        
# @lc code=end

