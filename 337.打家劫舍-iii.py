'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-27 14:34:20
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-27 15:12:45
FilePath: \Leetcode_Solver\337.打家劫舍-iii.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=337 lang=python3
#
# [337] 打家劫舍 III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        memo = dict()
        
        def treedp(root):
            # 不存在返回 0
            if not root:
                return 0
                        
            # 如果已经计算过了，直接返回
            if memo.get(root):
                return memo[root]
            
            # 叶子节点返回自己
            if not root.left and not root.right:
                return root.val
            
            # 非叶子递归计算即可
            res = root.val
            
            # 如果左右存在，就计算取本节点之后的状态
            if root.left:
                res += treedp(root.left.left) + treedp(root.left.right)
            if root.right:
                res += treedp(root.right.left) + treedp(root.right.right)

            # 和没有取本节点时的状态进行对比即可。
            res = max(res,treedp(root.left) + treedp(root.right))
            
            # 返回计算后结果
            memo[root] = res
            return res
        
        
        return treedp(root)
        
        
        
        
        
        
# @lc code=end

