'''
Author: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
Date: 2023-02-09 12:28:00
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2024-01-19 11:04:31
FilePath: \Leetcode_Solver\206.反转链表.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
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
        if head == None or head.next == None:
            return head

        last = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return last
    
    ###### 求解方法 2 
    #     p, rev = head, None
    #     while p:
    #         rev, rev.next, p = p, rev, p.next
    #     return rev
        
        
# @lc code=end

