'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-04-07 17:54:21
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-04-07 17:55:34
FilePath: \Leetcode_Solver\1161.最大层内元素和.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1161 lang=python3
#
# [1161] 最大层内元素和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        
        def level_order_travel(current_root, current_level, res) -> list:
            if not current_root:
                return res 
            if current_level == len(res):
                res.append([])
            
            res[current_level].append(current_root.val)
            
            if current_root.left:
                res = level_order_travel(current_root.left, current_level+1, res)
            if current_root.right:
                res = level_order_travel(current_root.right, current_level+1, res)
            
            return res
        
        ordered_res = level_order_travel(root, 0, [])  # list of lists of values, each sub list representing a level.
        
        level_sum = [sum(res) for res in ordered_res]
        
        return level_sum.index(max(level_sum)) + 1
        
        
        
# @lc code=end

