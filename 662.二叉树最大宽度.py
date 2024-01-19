'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-04-07 16:37:30
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-04-07 16:47:23
FilePath: \Leetcode_Solver\662.二叉树最大宽度.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=662 lang=python3
#
# [662] 二叉树最大宽度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def level_order_travel(current_root, current_level, current_pos, res) ->list:
            if not current_root:
                return res 
            if current_level == len(res):
                res.append([])
            
            res[current_level].append(current_pos)
            
            if current_root.left :
                res = level_order_travel(current_root.left, current_level+1, current_pos=current_pos*2, res = res)
            if current_root.right:
                res = level_order_travel(current_root.right, current_level+1, current_pos=current_pos*2+1, res = res)
            
            return res 

        level_order_res = level_order_travel(root,0,1,res=list())
        width = [res[-1] - res[0] +1 for res in level_order_res]
        
        return max(width)
        
# @lc code=end

