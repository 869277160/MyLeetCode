'''
Author: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
Date: 2023-02-10 14:51:39
LastEditors: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
LastEditTime: 2023-02-10 15:10:56
FilePath: \Leetcode_Solver\110.平衡二叉树.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=110 lang=python3
#
# [110] 平衡二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root == None : 
            return True
        if root.left == None and root.right == None :
            return True
        
        res = max(self.depth(root.left),self.depth(root.right)) - min(self.depth(root.left),self.depth(root.right)) 
        
        if res > 1 : return False 
        return self.isBalanced(root.right) and self.isBalanced(root.left);


        return res
        
        
    def depth(self, root: Optional[TreeNode]):
        
        if root == None:
            return 0
        # elif root.left == None and root.right == None :
        #     return level
        else :
            return max(self.depth(root.left)+1,self.depth(root.right)+1)

# @lc code=end

