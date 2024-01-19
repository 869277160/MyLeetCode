'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-20 14:19:50
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-20 14:24:13
FilePath: \Leetcode_Solver\237.删除链表中的节点.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=237 lang=python3
#
# [237] 删除链表中的节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        
        if node == None:
            return 
        else:
            
            # 要求本地修改
            # 需要通过赋值修改原有的节点
            p = node.next
            # 循环搜索到最后一个
            while(p.next != None):
                node.val = p.val
                node = node.next
                p = p.next
            
            # 放弃最后一个节点
            node.val = p.val
            node.next = None
            return
        
# @lc code=end

