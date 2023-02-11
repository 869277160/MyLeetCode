'''
Author: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
Date: 2023-02-10 11:58:25
LastEditors: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
LastEditTime: 2023-02-10 12:13:58
FilePath: \Leetcode_Solver\101.对称二叉树.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # 快速返回
        if root == None : return True

        # 复杂输入判断
        return self.isSymmetrcHelper(root.left,root.right)
    
    def isSymmetrcHelper(self, left, right):
        # 四种结果
        # 空分支
        if left == None and right == None: return True
        # 单一叶子
        if left == None or right == None or left.val != right.val: return False
        # 叶子
        # elif left.left == None and left.right == None and right.left == None and right.right == None and left.val == right.val: return True
        # # 中间节点递归判断
        return self.isSymmetrcHelper(left.left, right.right) and self.isSymmetrcHelper(left.right, right.left)

        
        
# @lc code=end

