'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-25 14:46:43
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-25 21:38:48
FilePath: \Leetcode_Solver\222.完全二叉树的节点个数.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=222 lang=python3
#
# [222] 完全二叉树的节点个数
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        
        if root == None:
            return 0
        if root.left == None and root.right == None:
            return 1
        # if root.left != None and root.right == None:
        #     return 1 + self.countNodes(root.left)
        # if root.left == None and root.right != None:
        #     return 1 + self.countNodes(root.right)
        # if root.left != None and root.right != None:
        #     return 1 + self.countNodes(root.left) + self.countNodes(root.right)
        
        
        left, right = root.left, root.right
        hl, hr = 0, 0
        while(left!=None):
            left = left.left
            hl +=1 
        while(left!=None):
            right = right.right
            hr +=1 
        if hl == hr:
            return 2**hl -1
        
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
        
        
# @lc code=end

