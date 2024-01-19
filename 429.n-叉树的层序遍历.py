'''
Author: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
Date: 2023-02-08 11:53:23
LastEditors: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
LastEditTime: 2023-02-08 12:00:08
FilePath: \Leetcode_Solver\429.n-叉树的层序遍历.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=429 lang=python3
#
# [429] N 叉树的层序遍历
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
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root == None:
            return []
        if root.children == None:
            return [[root.val]]

        output = self.levelOrderhelper(root=root, level=0, res=[[]])
        
        return output
 
    def levelOrderhelper(self, root, level=0, res=[[]]):
        # 返回原有结果即可
        if root == None:
            return res 
        # 判断是否是新的一层
        if len(res) == level:
            res.append([])
            
        # 类似先序遍历，先自己，之后左右，每一层的值都是物理上从左到右的。
        res[level] += [root.val]
        for child in root.children:
            res = self.levelOrderhelper(child, level+1, res)
        
        return res 

# @lc code=end

