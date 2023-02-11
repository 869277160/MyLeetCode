'''
Author: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
Date: 2023-02-10 11:36:43
LastEditors: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
LastEditTime: 2023-02-10 11:57:27
FilePath: \Leetcode_Solver\1669.合并两个链表.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1669 lang=python3
#
# [1669] 合并两个链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        
        if list1 == None: return list1
        if list2 == None: return list1
        
        
        p1 = list1
        p2 = list2 
        count = 0
        
        # 遍历list1
        while(p1 != None):
            # 刚开始
            if count < a-1:
                p1 = p1.next 
                count +=1 
            
            # 遍历到对应节点后进行操作
            elif count == a-1:
                temp = p1.next 
                p1.next = list2
                
                p1 = temp
                count +=1 
            
            # 让p1继续向前遍历，直到b
            elif count > a-1 and count < b:
                p1 = p1.next 
                count +=1 

            # 遍历完成之后接上对应节点后退出
            elif count == b:
                
                # p2 到尾部节点
                while(p2.next != None):
                    p2 = p2.next 
                
                # 这时 p1在b, p2 遍历到尾部后应接上p1 next
                # 同时断开原有p1
                p2.next = p1.next
                p1.next = None 
                
                return list1
                pass 
        
        
        
        
        
        
        
# @lc code=end

