'''
Author: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
Date: 2023-02-10 09:52:30
LastEditors: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
LastEditTime: 2023-02-10 10:08:37
FilePath: \Leetcode_Solver\141.环形链表.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=141 lang=python3
#
# [141] 环形链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        if head == None: return False 
        if head == head.next: return True 
        if head.next == None: return False 
        if head.next.next == head : return True 
        
        fast = head 
        slow = head 
        
        # 快慢指针搜索 
        # 利用快指针作为条件
        while(fast != None and fast.next != None):
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                return True 

        return False 
        
        
        
        
        
        
        
        
# @lc code=end

