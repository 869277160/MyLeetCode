'''
Author: DingWang wangding19@mails.ucas.ac.cn
Date: 2024-01-27 17:39:02
LastEditors: DingWang wangding19@mails.ucas.ac.cn
LastEditTime: 2024-01-27 17:59:14
FilePath: \Leetcode_Solver\437.路径总和-iii.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=437 lang=python3
#
# [437] 路径总和 III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if root == None:
            return 0
        else:
            # print(root.val, targetSum)
            res = self.rootSum(root, targetSum)
            res_3 = self.pathSum(root.left, targetSum) 
            res_4 = self.pathSum(root.right, targetSum)
            
            res += res_3 + res_4
                
            return res
    
    def rootSum(self, root, targetSum):
        if root is None:
            return 0

        ret = 0
        if root.val == targetSum:
            ret += 1

        ret += self.rootSum(root.left, targetSum - root.val)
        ret += self.rootSum(root.right, targetSum - root.val)
        return ret



        
        
        
# @lc code=end

