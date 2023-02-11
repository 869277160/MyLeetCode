'''
Author: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
Date: 2023-02-11 15:29:19
LastEditors: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
LastEditTime: 2023-02-11 15:42:39
FilePath: \Leetcode_Solver\257.二叉树的所有路径.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=257 lang=python3
#
# [257] 二叉树的所有路径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        if root == None : return []
        if root != None and root.left == None and root.right == None: return [str(root.val)]
        
        return self.helper(root, "", [])
        
    
    def helper(self, root, path, res):
        if root == None :
            return res
        
        if path == "": 
            path = path + f"{root.val}"
        else :
            path = path + f"->{root.val}"
            
            
        if root.left == None and root.right == None:
            res.append(path)
            return  res
        
        if root.left != None and root.right == None:
            return self.helper(root.left,path,res)
        
        if root.left == None and root.right != None:
            return self.helper(root.right,path,res)
        
        if root.left != None and root.right != None:
            res = self.helper(root.left,path,res)
            res = self.helper(root.right,path,res)
            return res
        
# @lc code=end

