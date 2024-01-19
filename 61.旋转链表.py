'''
Author: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
Date: 2023-02-06 21:41:10
LastEditors: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
LastEditTime: 2023-02-06 22:04:29
FilePath: \Leetcode_Solver\61.旋转链表.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=61 lang=python3
#
# [61] 旋转链表
#

# @lc code=start
# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if head == None or head.next == None or k == 0:
            return head 
       
        total_len =1 
        counter = head 
        while(counter.next != None):
            total_len +=1 
            counter=counter.next
        counter.next = head

        if k == total_len:
            return head
        if k > total_len:
            k = k % total_len
            
        for i in range(total_len-k):
            counter = counter.next;
        newHead = counter.next;
        counter.next = None
        
        return newHead; 
# @lc code=end

