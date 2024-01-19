'''
Author: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
Date: 2023-02-08 11:46:58
LastEditors: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
LastEditTime: 2023-02-08 11:51:33
FilePath: \Leetcode_Solver\589.n-叉树的前序遍历.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=589 lang=python3
#
# [589] N 叉树的前序遍历
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
    def preorder(self, root: 'Node') -> List[int]:
        
        # 结果返回
        res = []
        
        # 结束条件 
        if root == None:
            return []
        if root.children == None:
            return [root.val] 
        
        # 进一步搜索
        res += [root.val]
        for node in root.children:
            res += self.preorder(node)

        return res 
    
        
        
        
        
        
        
# @lc code=end

