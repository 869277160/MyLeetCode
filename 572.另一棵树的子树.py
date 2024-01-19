'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-22 11:23:49
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-22 11:33:40
FilePath: \Leetcode_Solver\572.另一棵树的子树.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=572 lang=python3
#
# [572] 另一棵树的子树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if self.isSame(root, subRoot):
            return True
        if root == None:
            return False
        else :
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

        
    def isSame(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root == None and subRoot == None: 
            return True
        elif (root == None and subRoot != None) :
            return False
        elif (root != None and subRoot == None) :
            return False
        elif root.val != subRoot.val :
            return False 

        return self.isSame(root.left, subRoot.left) and self.isSame(root.right, subRoot.right)
    
        
        
        
                
        
        # else :
        #     if root.left == None and root.right == None and subRoot.left == None and subRoot.right == None:
        #         return root.val == subRoot.val
        #     elif root.left == None and root.right == None and subRoot.left == None and subRoot.right != None:
        #         return False
        #     elif root.left == None and root.right == None and subRoot.left != None and subRoot.right == None:
        #         return False
        #     elif root.left != None and root.right == None and subRoot.left != None and subRoot.right == None:
        #             return False
        #     elif root.left == None and root.right != None and subRoot.left != None and subRoot.right == None:
        #                 return False
                    
           
        #         return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        #     else :
        #         if 
        #             return True
        #         else :
    
        # [1,1]\n [1]
# @lc code=end

