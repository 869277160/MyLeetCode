'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-16 23:18:01
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-16 23:27:39
FilePath: \Leetcode_Solver\872.叶子相似的树.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=872 lang=python3
#
# [872] 叶子相似的树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if root1 == None and root2 == None:
            return False
        if root1 != None and root2 == None:
            return False
        if root1 == None and root2 != None:
            return False
        
        res1 = self.getleaf(root1)
        res2 = self.getleaf(root2)
        
        return res1 == res2        
        
    def getleaf(self, root, res=[]):
        if root == None:
            return res 

        if root.left == None and root.right == None:
            return res + [root.val]
        if root.left != None and root.right == None:
            return self.getleaf(root.left,res)
        if root.left == None and root.right != None:
            return self.getleaf(root.right,res)
        if root.left != None and root.right != None:
            # res = res + [root.val]
            res = self.getleaf(root.left,res)
            res = self.getleaf(root.right,res)
            return res 
# @lc code=end

