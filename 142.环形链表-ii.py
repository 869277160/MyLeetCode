'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-21 11:26:11
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-21 11:30:16
FilePath: \Leetcode_Solver\142.环形链表-ii.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=142 lang=python3
#
# [142] 环形链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast,slow = head, head 
        
        
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return fast
        
        
        
        
        
        
# @lc code=end

