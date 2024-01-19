'''
Author: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
Date: 2023-02-06 22:05:31
LastEditors: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
LastEditTime: 2023-02-07 09:27:38
FilePath: \Leetcode_Solver\86.分隔链表.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=86 lang=python3
#
# [86] 分隔链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head 
        
        # // 存放小于 x 的链表的虚拟头结点
        dummy1 = ListNode(-1);
        # // 存放大于等于 x 的链表的虚拟头结点
        dummy2 = ListNode(-1);
        # // p1, p2 指针负责生成结果链表
        p1, p2 = dummy1,dummy2;
        # // p 负责遍历原链表，类似合并两个有序链表的逻辑
        # // 这里是将一个链表分解成两个链表
        p = head;
        while(p != None):
            if (p.val >= x):
                p2.next = p;
                p2 = p2.next;
            else :
                p1.next = p;
                p1 = p1.next;
            # // 断开原链表中的每个节点的 next 指针
            temp = p.next;
            p.next = None;
            p = temp;

        # // 连接两个链表
        p1.next = dummy2.next;

        return dummy1.next;

# @lc code=end

