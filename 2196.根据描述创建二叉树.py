'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-13 16:52:14
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-13 17:17:33
FilePath: \Leetcode_Solver\2196.根据描述创建二叉树.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2196 lang=python3
#
# [2196] 根据描述创建二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        
        parents = set()
        children = set()
        node_dict = {}
        
        
        for description in descriptions:
            parents.add(description[0])
            children.add(description[1])
            
            if description[0] not in node_dict.keys():
                node_dict[description[0]] = TreeNode(description[0])
            if description[1] not in node_dict.keys():
                node_dict[description[1]] = TreeNode(description[1])
            if description[2] == 1:
                node_dict[description[0]].left = node_dict[description[1]]
            else: 
                node_dict[description[0]].right = node_dict[description[1]]
        
        root_num = (set(parents) - set(children)).pop()

        # root = TreeNode(root_num)
        # root.left = self.buildTree(descriptions, root_num, is_left=True)
        # root.right = self.buildTree(descriptions, root_num, is_left=False)

        return node_dict[root_num] 
    
        # current_pos = root
        # while(descriptions != []):
        #     for description in descriptions:
        #         if description[0] == current_pos.val:
        #             if description[2] == 1 :
        #                 current_pos.left = TreeNode(description[1])
        #             else :
        #                 current_pos.right = TreeNode(description[1])
        #             descriptions.remove(description)
        #     if current_pos.left != None:
        #         current_pos = current_pos.left
        #     else:
        #         current_pos = current_pos.right 
                
    # def buildTree(self, descriptions: List[List[int]], root_num: int, is_left:bool ) -> Optional[TreeNode]:
        
    #     for description in descriptions:
    #         if description[0] == root_num and description[2] == is_left:
    #             current_node = TreeNode(description[1])
    #             current_node.left = self.buildTree(descriptions, current_node.val, is_left=True)
    #             current_node.right = self.buildTree(descriptions, current_node.val, is_left=False)
    #             return current_node
        
    #     return None 


        
        
# @lc code=end

