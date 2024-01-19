'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-07 17:11:32
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-14 09:13:16
FilePath: \Leetcode_Solver\1022.从根到叶的二进制数之和.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1022 lang=python3
#
# [1022] 从根到叶的二进制数之和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        
        if root == None :
            return 0
        if root.left == None and root.right == None:
            return root.val
        else:
            return self.sumTree(root, current_num=0, total=0)
             


    def sumTree(self,root, current_num, total)->int:
        
        if root == None:
            return total
        else:
            current_num = current_num*2 + root.val 
            if root.left == None and root.right == None:
                total += current_num
                return total 
            elif root.left == None and root.right != None:
                right_total = self.sumTree(root.right,current_num,total)
                return right_total
            elif root.left != None and root.right == None:
                left_total = self.sumTree(root.left,current_num,total)
                return left_total
            elif root.left != None and root.right != None:
                left_total = self.sumTree(root.left,current_num,total)
                right_total = self.sumTree(root.right,current_num,total)
                return left_total + right_total
        

    # def sumAll(self, root, current_path, total) -> int:
    #     if root == None :
    #         return total
        
    #     current_path+=str(root.val)
    #     if root.left == None and root.right == None:
    #         total += int(current_path,2)
    #         return total
    #     elif root.left != None and root.right == None:
    #         # current_path += str(root.val)
    #         return self.sumAll(root.left, current_path, total)
        
    #     elif root.left == None and root.right != None:
    #         # current_path += str(root.val)
    #         return self.sumAll(root.right, current_path, total)
        
    #     else:
    #         # current_path += str(root.val)
    #         return self.sumAll(root.left, current_path, total) + self.sumAll(root.right, current_path, total)
        
# @lc code=end

