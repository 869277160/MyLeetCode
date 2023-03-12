'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-25 20:25:04
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-25 20:41:31
FilePath: \Leetcode_Solver\95.不同的二叉搜索树-ii.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=95 lang=python3
#
# [95] 不同的二叉搜索树 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0 : 
            return None 
        if n == 1 : 
            return [TreeNode(1)]
        if n == 2 : 
            return [TreeNode(1,right=TreeNode(2)),TreeNode(2,left=TreeNode(1))]
        else:
            return self.generateSubTree(low=1,high=n)
    
    # 生成所有符合条件的二叉搜索树
    def generateSubTree(self,low:int,high:int) -> TreeNode:
        res = []
        if low > high :
            res.append(None)
            return res 
        else:
           
            # 不断增加左子树上的节点数
            for i in range(low,high+1):
                # 生成左子树 
                left = self.generateSubTree(low=low,high=i-1)
                # 生成右子树 []
                right = self.generateSubTree(low=i+1,high=high)
                # 左右子树组合
                for l in left:
                    for r in right:
                        root = TreeNode(i)
                        root.left = l
                        root.right = r
                        res.append(root)

        return res
        

# @lc code=end

