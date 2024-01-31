'''
Author: DingWang wangding19@mails.ucas.ac.cn
Date: 2024-01-27 17:06:13
LastEditors: DingWang wangding19@mails.ucas.ac.cn
LastEditTime: 2024-01-27 17:38:00
FilePath: \Leetcode_Solver\501.二叉搜索树中的众数.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=501 lang=python3
#
# [501] 二叉搜索树中的众数
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import Counter
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        self.res = []
        self.traverse(root)
        # print(Counter(self.res))
        counter = Counter(self.res)
        max_count = counter.most_common(1)[0][1]
        # print(max_count)
        # for item in counter:
        #     print(item)
        #     print(counter[item])
        res = [item for item in counter if counter[item]==max_count]
        return res


    def traverse(self, root):
        if root == None:
            return 

        self.traverse(root.left)
        self.res.append(root.val)
        self.traverse(root.right)

        
        
        
# @lc code=end

