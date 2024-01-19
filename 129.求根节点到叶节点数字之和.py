'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-13 16:36:28
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-13 16:44:34
FilePath: \Leetcode_Solver\129.求根节点到叶节点数字之和.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=129 lang=python3
#
# [129] 求根节点到叶节点数字之和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        else :
            return self.sumTree(root,current_num=0,total=0)

    def sumTree(self,root, total):
        
        if root == None:
            return total
        else:
            current_num = total*10 + root.val 
            if root.left == None and root.right == None:
                total += current_num
                return total 
            elif root.left == None and root.right != None:
                right_total = self.sumTree(root.right,current_num,total)
                return right_total
            elif root.left != None and root.right == None:
                left_total = self.sumTree(root.left,current_num,total)
                return left_total
            elif root.left != None and root.right != None:
                left_total = self.sumTree(root.left,current_num,total)
                right_total = self.sumTree(root.right,current_num,total)
                return left_total + right_total
        
# @lc code=end

