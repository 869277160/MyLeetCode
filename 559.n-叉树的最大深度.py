'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-20 09:36:39
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-20 09:45:17
FilePath: \Leetcode_Solver\559.n-叉树的最大深度.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=559 lang=python3
#
# [559] N 叉树的最大深度
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        
        if root == None :
            return 0
        
        if root.children == None :
            return 1
        else:
            max_depth = 0
            for child in root.children:
                max_depth = self.maxDepth(child) +1 if self.maxDepth(child) +1 > max_depth else max_depth
            return 1 if max_depth == 0 else max_depth
            
            

        
        
# @lc code=end

