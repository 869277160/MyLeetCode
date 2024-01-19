'''
Author: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
Date: 2023-02-05 15:42:16
LastEditors: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
LastEditTime: 2023-02-05 15:52:17
FilePath: \Leetcode_Solver\203.移除链表元素.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=203 lang=python3
#
# [203] 移除链表元素
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    # TODO: 需要重新刷一次
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head == None:
            return None
        FakeHead = ListNode(-2423,head)
        p = FakeHead
        while(p.next != None):
            if p.next.val == val:
                p.next = p.next.next
            # if p.next.val == val:
            #     p.next = None
            else:
                p = p.next 

        return FakeHead.next 
# @lc code=end


#         ListNode prev = dummyHead;
#         while (prev.next != null)
#         {
#             if (prev.next.val == val)
#                 prev.next = prev.next.next;
#             else
#                 prev = prev.next;
#         }
#         return dummyHead.next;
#     }
# }