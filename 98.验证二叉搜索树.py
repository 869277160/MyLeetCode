'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-25 14:47:40
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-25 19:26:10
FilePath: \Leetcode_Solver\98.验证二叉搜索树.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left 
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def helper(root, current_min, current_max):
            if root == None :
                return True 
            else :
                # 判断当前节点是否符合条件
                if current_max != None and root.val >= current_max:
                    return False
                if current_min != None and root.val <= current_min:
                    return False
                # 节点符合最大最小值条件，继续判断左右子树
                if root.val > current_min and root.val < current_max:
                    
                    return helper(root.left, current_min, root.val) and helper(root.right, root.val, current_max)
                
            
            
            return  True 
        
        
        if root == None :
            return True
        else:
            if root.left == None and root.right == None:
                return True 
            else:
                return helper(root.left, float("-inf"), root.val) and helper(root.right, root.val, float("inf"))
            

        
# @lc code=end

