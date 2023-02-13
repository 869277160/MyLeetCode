'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-11 15:43:55
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-11 16:05:45
FilePath: \Leetcode_Solver\606.根据二叉树创建字符串.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
'''
Author: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
Date: 2023-02-11 15:43:55
LastEditors: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
LastEditTime: 2023-02-11 15:56:36
FilePath: \Leetcode_Solver\606.根据二叉树创建字符串.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=606 lang=python3
#
# [606] 根据二叉树创建字符串
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if root == None:
            return ""
        
        return self.tree2strHelper(root,"")
        

    
    def tree2strHelper(self,root,res):
        # 叶子返回
        if root == None:
            return res
        
        # 叶子节点
        if root.left == None and root.right == None:
            res= res + f"{root.val}"
            return res
        
        # 右边空
        if root.left != None and root.right == None:
            res = res + f"{root.val}" + "(" + self.tree2strHelper(root.left,res) + ")"
            return res
        # 左边空
        if root.left == None and root.right != None:
            res += f"{root.val}" + "()" + "(" + self.tree2strHelper(root.right,res)+ ")"
            return res 
        # 左右都不空
        if root.left != None and root.right != None:
            res += f"{root.val}" + "(" + self.tree2strHelper(root.left,res)+ ")" + "(" +self.tree2strHelper(root.right,res)+ ")"
            return res
        
# @lc code=end

