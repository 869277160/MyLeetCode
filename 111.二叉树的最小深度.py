'''
Author: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
Date: 2023-02-10 22:56:15
LastEditors: DingWang wangding19@mails.ucas.ac.cn
LastEditTime: 2024-01-22 14:56:55
FilePath: \Leetcode_Solver\111.二叉树的最小深度.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        
        ##### Solver 1 递归求解，对比返回最小的，dfs
        # if root == None: 
        #     return 0
        # else :
        #     if root.left == None and root.right == None : 
        #         return 1 
        #     if root.left == None and root.right != None : 
        #         return self.minDepth(root.right) + 1
        #     if root.left != None and root.right == None : 
        #         return self.minDepth(root.left) + 1
        #     if root.left != None and root.right != None : 
        #         return min(self.minDepth(root.left) + 1, self.minDepth(root.right) + 1)
        
        
        ##### Solver 2 bfs 求解
        # from collections import Queue
        from typing import Optional
        from queue import Queue
        
        # 初始化队列
        if not root: 
            return 0
        q = Queue()
        
        # 访问最初节点
        q.put(root)
        depth = 1 
        
        # 迭代求解
        while not q.empty():
            # 访问剩下节点
            q_size = q.qsize()
            for i in range(q_size):
                # 获取当前节点
                current_node = q.get()
                
                # 结束条件判断
                if current_node.left == None and current_node.right == None:
                    return depth
                
                # 将节点的邻居入队
                if current_node.left:
                    q.put(current_node.left)
                if current_node.right:
                    q.put(current_node.right)
            # 结果+1
            depth += 1
        return depth
# @lc code=end

