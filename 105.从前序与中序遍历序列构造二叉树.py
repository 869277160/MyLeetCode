'''
Author: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
Date: 2023-02-10 12:14:55
LastEditors: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
LastEditTime: 2023-02-10 14:36:38
FilePath: \Leetcode_Solver\105.从前序与中序遍历序列构造二叉树.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=105 lang=python3
#
# [105] 从前序与中序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        # 利用list切片进行迭代即可
        if len(preorder) == 0:  return None
        if len(inorder) == 0 : return None 
        # if len(preorder) == 1 : return TreeNode(preorder[0])
        # if len(inorder) == 1 : return TreeNode(preorder[0])
        
        restree = TreeNode(preorder[0])
        left_tree_size = -1
        root_index = -1
        for i in range(len(inorder)):
            if inorder[i] == preorder[0]:
                root_index = i
                left_tree_size = root_index
        
        restree.left = self.buildTree(preorder[1:left_tree_size+1],inorder[:root_index])
        restree.right = self.buildTree(preorder[left_tree_size+1:], inorder[root_index+1:])

        return restree
    
    # # 通过index 判断当前用于构造子树的序列
    # def build(self, preorder, preStart, preEnd,inorder, inStart, inEnd):
        
    #     if (preStart > preEnd):  return None 
        
    #     for i in range(inStart,inEnd+1):
    #         if inorder[i] == preorder[0]:
    #             root_inorder_index = i

    #             leftSize = root_inorder_index - inStart;
                
                

    #             return restree
  
        
        
# @lc code=end

