'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-24 10:14:47
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-24 11:12:19
FilePath: \Leetcode_Solver\19.删除链表的倒数第-n-个结点.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第 N 个结点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
    #     # get length  
    #     p = head 
    #     length = 0
    #     while p :
    #         p = p.next 
    #         length += 1 
        
        
    #     if length == n:
    #         return head.next
    #     else :
    #         p = head 

    #         # 遍历到倒数第n个节点的前一个节点
    #         for i in range(length - n - 1):
    #             p = p.next
            
    #         # 跳过特定节点
    #         p.next = p.next.next
    #         return head
        
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # get the last n of the list 
        
        dummy = ListNode(0,head)
        
        fast = dummy
        for i in range(n):
            fast = fast.next 
        
        slow = dummy
        while(fast.next):
            fast = fast.next
            slow = slow.next 
        
        slow.next = slow.next.next
        
        return dummy.next
        
        
        
        
        
        
# @lc code=end

