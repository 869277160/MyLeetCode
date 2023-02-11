'''
Author: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
Date: 2023-02-05 15:19:44
LastEditors: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
LastEditTime: 2023-02-05 15:23:35
FilePath: \Leetcode_Solver\160.相交链表.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=160 lang=python3
#
# [160] 相交链表
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 让两个链表指针的长度同时变成 A + B 和 B + A。如果有链表交点，那么两个搜索指针会在交点处相遇
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None
        
        pA, pB = headA, headB
        # # 如果没有相交，那么pA和pB会同时为None
        while(pA != pB):
            # 如果没有遍历完成当前链表则继续遍历，否则遍历另一个链表
            pA = pA.next if pA else headB
            pB = pB.next if pB else headA
        return pA 
        
        
# @lc code=end

