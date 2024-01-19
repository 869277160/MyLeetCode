'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-12 15:15:47
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-25 21:47:52
FilePath: \Leetcode_Solver\889.根据前序和后序遍历构造二叉树.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=889 lang=python3
#
# [889] 根据前序和后序遍历构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# NOTE: 本题的关键在于理解前序遍历和后序遍历的特点，一个是左右根，一个是根左右，因此可以利用这个特点进行递归
# NOTE: 切片的使用 ： 前闭后开!!!!!
class Solution:
    # def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
    #     # 利用list切片进行迭代即可
        
    #     # 结束条件
    #     if len(preorder) == 0:  return None
    #     if len(postorder) == 0 : return None 
    #     if len(preorder) == 1 or len(postorder) == 1 : 
    #         val = preorder[0] if len(preorder) == 1 else postorder[0]
    #         return TreeNode(val) 

    #     if len(preorder) == 2 and len(postorder) == 2:
    #         restree = TreeNode(preorder[0])
    #         restree.left = TreeNode(preorder[1])
    #         restree.right = None
    #         return restree
         
    #     if len(preorder) == 3 and len(postorder) == 3:
    #         restree = TreeNode(preorder[0])
    #         if preorder[1] == postorder[0]:
    #             restree.left = TreeNode(preorder[1])
    #             restree.right = TreeNode(preorder[2])
    #         else:
    #             restree.left = TreeNode(preorder[1],TreeNode(preorder[2]))
    #             restree.right = None
    #         return restree


    #     if len(preorder) > 3 and len(postorder) > 3:
    #         # 应该有两个节点，需要判断左右并返回
    #         if preorder[1] != postorder[-2]:
    #             left_root_index = self.Getindex(postorder , preorder[1])
    #             right_root_index = self.Getindex(preorder , postorder[-2])
    #             if left_root_index == -1 and right_root_index == -1:
    #                 return None
    #             else :
    #                 left_tree_size = left_root_index + 1
    #                 right_tree_size = len(preorder) - left_tree_size
                    
    #                 restree = TreeNode(preorder[0])
    #                 restree.left = self.constructFromPrePost(preorder[1:left_tree_size],postorder[:left_tree_size+1])
    #                 restree.right = self.constructFromPrePost(preorder[-(right_tree_size):],postorder[-(1+right_tree_size):-1])

    #                 return restree

    #         # 否则只有一个子树节点，那么直接作为左节点返回或者右节点返回
    #         else:
    #             restree = TreeNode(preorder[0])
    #             restree.left = self.constructFromPrePost(preorder[1:],postorder[:-1])
    #             restree.right = None
    #             return restree
            

    # def Getindex(self,input_list,val):
        
    #     if len(input_list) == 0:
    #         return -1 
    #     elif len(input_list) == 1:
    #         if input_list[0] == val:
    #             return 0
    #         else:
    #             return -1
    #     else :
    #         for i in range(len(input_list)):
    #             if input_list[i] == val:
    #                 return i
        
    #     return -1
        

    def constructFromPrePost(self, pre, post):
        if not pre: return None
        root = TreeNode(pre[0])
        if len(pre) == 1: return root

        L = post.index(pre[1]) + 1
        root.left = self.constructFromPrePost(pre[1:L+1], post[:L])
        root.right = self.constructFromPrePost(pre[L+1:], post[L:-1])
        return root

# @lc code=end

