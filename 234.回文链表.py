'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-10 10:09:47
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-15 17:22:49
FilePath: \Leetcode_Solver\234.回文链表.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=234 lang=python3
#
# [234] 回文链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False 
        if head.next == None :
            return True
        if head.next.next == False:
            if  head.val != head.next.val:
                return False 
            else :
                return True 
        
        res = []
        p = head 
        
        while(p):
            res.append(p.val)
            p=p.next
        
        return res == res[::-1]
# @lc code=end

