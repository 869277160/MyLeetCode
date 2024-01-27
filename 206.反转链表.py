'''
Author: DingWang wangding19@mails.ucas.ac.cn
Date: 2024-01-18 22:42:06
LastEditors: DingWang wangding19@mails.ucas.ac.cn
LastEditTime: 2024-01-19 15:21:31
FilePath: \Leetcode_Solver\206.反转链表.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        ###  Solver 1 基于递归的反转       ###############
        # 是否是单个元素的链表
        # if head == None or head.next == None:
        #     return head

        # rest = self.reverseList(head.next)
        # head.next.next = head
        # head.next = None
        # return rest
        
        
        
        ###  Solver 2 基于遍历的反转       ###############
        if head == None or head.next == None:
            return head

        p, rev = head, None
        while p:
            rev, rev.next, p = p, rev, p.next
        return rev


# @lc code=end

