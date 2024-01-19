'''
Author: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
Date: 2023-02-09 09:44:30
LastEditors: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
LastEditTime: 2023-02-09 09:49:17
FilePath: \Leetcode_Solver\100.相同的树.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=100 lang=python3
#
# [100] 相同的树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # 条件：两个树的根节点值相同，且左子树和右子树也相同
        # 根节点判断是否相同
        if p == None and q == None:
            return True
        
        if p == None or q == None:
            return False
        if p.val != q.val:
            return False
        
        # 递归左右子树
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        
# @lc code=end

