'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-22 11:37:18
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-22 11:38:21
FilePath: \Leetcode_Solver\117.填充每个节点的下一个右侧节点指针-ii.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=117 lang=python3
#
# [117] 填充每个节点的下一个右侧节点指针 II
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
# 类似层序遍历，
# 但是每一层的节点不一定是满的，所以需要判断节点是否为空
# 或者直接初始化为空，有则填充
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        if root == None :
            return root 
        else :
            
        
        
        
# @lc code=end

