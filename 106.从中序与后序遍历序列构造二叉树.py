'''
Author: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
Date: 2023-02-10 14:36:42
LastEditors: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
LastEditTime: 2023-02-10 14:42:37
FilePath: \Leetcode_Solver\106.从中序与后序遍历序列构造二叉树.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=106 lang=python3
#
# [106] 从中序与后序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        # 和之前的题目思路相同，改下变量还有计算方式即可
        if len(inorder) == 0:  return None
        if len(postorder) == 0 : return None 
    
        restree = TreeNode(postorder[-1])
        left_tree_size = -1
        root_index = -1
        for i in range(len(inorder)):
            if inorder[i] == postorder[-1]:
                root_index = i
                left_tree_size = root_index
        
        restree.left = self.buildTree(inorder[:root_index],postorder[:left_tree_size],)
        restree.right = self.buildTree(inorder[root_index+1:],postorder[left_tree_size:-1],)

        return restree
    
# @lc code=end

