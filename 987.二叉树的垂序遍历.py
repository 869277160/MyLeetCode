'''
Author: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
Date: 2023-02-08 12:01:23
LastEditors: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
LastEditTime: 2023-02-08 13:19:05
FilePath: \Leetcode_Solver\987.二叉树的垂序遍历.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=987 lang=python3
#
# [987] 二叉树的垂序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# class Solution:
#     def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
#         if root == None: return []
#         if root.left == None and root.right == None: return [[root.val]]
        
#         max_wide = -10000
#         min_wide = 10000
#         max_depth = -10000
#         min_depth = 10000
#         res, max_wide,min_wide,max_depth,min_depth = self.verticalTraversalHelper(root)
        
#         res = [[node[0],node[1],node[2]-min_wide] for node in res]
        
#         output = []
#         for _ in range((max_wide-min_wide)+1):
#             output.append([])
        
#         for node in res :
#             output[node[2]].append(node[0])
        
#         # 重排序输出
#         for i in range(len(output)):
#             output[i]=sorted(output[i])
 
#         return output
    
#     # 
#     # 先序遍历(任何一种遍历即可，注意控制depth和wide)，返回必要信息用于后续转化
#     def verticalTraversalHelper(self,root,depth=0, wide=0, res=[] ,max_wide=0,min_wide=0,max_depth=0,min_depth=0):
        
#         # 返回原有结果即可
#         if root == None:
#             return res,max_wide,min_wide,max_depth,min_depth 
        
#         max_wide = max(max_wide,wide)
#         min_wide = min(min_wide,wide)
#         max_depth = max(max_depth,depth)
#         min_depth = min(min_depth,depth)
        
#         # 先序遍历
#         res += [[root.val,depth,wide]]
#         res,max_wide,min_wide,max_depth,min_depth = self.verticalTraversalHelper(root.left, depth+1, wide-1,res,max_wide,min_wide,max_depth,min_depth)
#         res,max_wide,min_wide,max_depth,min_depth = self.verticalTraversalHelper(root.right, depth+1, wide+1,res,max_wide,min_wide,max_depth,min_depth)
        
        
#         return res,max_wide,min_wide,max_depth,min_depth 
        
        
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        nodes = list()

        def dfs(node: TreeNode, row: int, col: int) -> None:
            if not node:
                return

            nodes.append((col, row, node.val))
            dfs(node.left, row + 1, col - 1)
            dfs(node.right, row + 1, col + 1)

        dfs(root, 0, 0)
        nodes.sort()
        ans, lastcol = list(), float("-inf")

        for col, row, value in nodes:
            if col != lastcol:
                lastcol = col
                ans.append(list())
            ans[-1].append(value)
        
        return ans


# @lc code=end

