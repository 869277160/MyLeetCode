'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-19 15:12:22
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-19 15:22:08
FilePath: \Leetcode_Solver\83.删除排序链表中的重复元素.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=83 lang=python3
#
# [83] 删除排序链表中的重复元素
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head == None or head.next == None :
            return head 
        if head != None and head.next!= None and head.next.next == None :
            if head.val == head.next.val:
                return head.next
            else :
                return head 
        
        # 双指针之快慢指针，快指针遍历链表，慢指针指向当前不重复的节点
        res = ListNode(0,head)
        p_res = res.next 
        p = head
        
        
        while(p != None ):
            if p.val != p_res.val:
                p_res.next = p
                p_res = p_res.next

            p = p.next

        # 注意结束的时候将剩下部分断开
        p_res.next = None
        return res.next
        
        
        
# @lc code=end

