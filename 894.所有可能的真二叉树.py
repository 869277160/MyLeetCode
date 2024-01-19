'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-04-07 16:54:38
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-04-07 17:08:55
FilePath: \Leetcode_Solver\894.所有可能的真二叉树.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=894 lang=python3
#
# [894] 所有可能的真二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        
        possible = [[] for i in range(21)]
        possible[1] = [TreeNode(0)]
        possible[3] = [TreeNode(0, TreeNode(0), TreeNode(0))]
        
        if n % 2 == 0:
            return []
        
        for i in range(5,n+1,2):
            for j in range(1,i,2):
                for left in possible[j]:
                    for right in possible[i-j-1]:
                            possible[i].append(TreeNode(0,left,right))
                
        
        return possible[n]
        
# @lc code=end

