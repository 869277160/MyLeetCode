'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-20 15:05:50
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-20 15:09:47
FilePath: \Leetcode_Solver\938.二叉搜索树的范围和.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=938 lang=python3
#
# [938] 二叉搜索树的范围和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        if root == None:
            return 0
        
        res = root.val if root.val>= low and root.val<=high else 0
        
        if root.left == None and root.right == None :
            return res
        
        if root.left != None and root.right == None :
            res += self.rangeSumBST(root.left,low,high)
            return res
        
        if root.left == None and root.right != None :
            res += self.rangeSumBST(root.right,low,high)
            return res
        
        if root.left != None and root.right != None :
            res += self.rangeSumBST(root.left,low,high)
            res += self.rangeSumBST(root.right,low,high)
            return res
        
# @lc code=end

