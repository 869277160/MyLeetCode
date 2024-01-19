'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-17 10:55:28
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-17 10:59:53
FilePath: \Leetcode_Solver\876.链表的中间结点.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=876 lang=python3
#
# [876] 链表的中间结点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast, slow = head, head
        
        while(fast):
            if fast.next == None:
                return slow
            else:
                if fast.next.next == None:
                    return slow.next
                else :
                    fast = fast.next.next
                    slow = slow.next
            
        
# @lc code=end

