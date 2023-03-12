'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-18 14:25:49
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-18 15:42:16
FilePath: \Leetcode_Solver\1721.交换链表中的节点.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1721 lang=python3
#
# [1721] 交换链表中的节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        # get the length for the list 
        length = 0
        p = head
        while(p):
            length += 1
            p = p.next
        
        
        if length == 1: return head
        starter ,ender = 0, 0
        starter_p, ender_p = head, head
        
        while(starter != 0 and ender != 0):
            starter_p = starter_p.next
            ender_p = ender_p.next
            starter += 1
            ender += 1
        
        # if length == 2: return head.next
        
        
# @lc code=end

