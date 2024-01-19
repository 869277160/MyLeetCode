'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-25 20:42:24
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-25 21:00:17
FilePath: \Leetcode_Solver\1008.前序遍历构造二叉搜索树.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1008 lang=python3
#
# [1008] 前序遍历构造二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        # 二叉搜索树的前序遍历
        
        if len(preorder) == 0:
            return None 
        elif len(preorder) == 1:
            return TreeNode(preorder[0])
        elif len(preorder) == 2:
            if preorder[0] > preorder[1]:
                return TreeNode(preorder[0],left=TreeNode(preorder[1]))    
            else :
                return TreeNode(preorder[0],right=TreeNode(preorder[1]))    
        else :
            root = TreeNode(preorder[0])
            for i in range(len(preorder)):
                if preorder[i] > preorder[0]:
                    root.left = self.bstFromPreorder(preorder[1:i])
                    root.right = self.bstFromPreorder(preorder[i:])
                    return root
                
            root.left = self.bstFromPreorder(preorder[1:])
            root.right = None 
            return root
        
        
        
# @lc code=end

