'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-25 21:01:16
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-25 21:04:27
FilePath: \Leetcode_Solver\700.二叉搜索树中的搜索.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=700 lang=python3
#
# [700] 二叉搜索树中的搜索
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        if root == None :
            return None 
        else :
            if root.val == val :
                return root 
            else:
                if root.left == None and root.right == None :
                    return None
                if root.left != None and root.right == None :
                    if root.val < val:
                        return None 
                    else :
                        return self.searchBST(root.left,val)
                if root.left == None and root.right != None :
                    if root.val < val:
                        return self.searchBST(root.right,val)
                    else :
                        return None 
                if root.left != None and root.right != None :
                    if root.val < val:
                        return self.searchBST(root.right,val)
                    else :
                        return self.searchBST(root.left,val)

        

        
# @lc code=end

