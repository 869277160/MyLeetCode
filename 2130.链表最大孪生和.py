'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-20 15:12:47
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-20 15:14:26
FilePath: \Leetcode_Solver\2130.链表最大孪生和.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2130 lang=python3
#
# [2130] 链表最大孪生和
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        res = []
        sum_res = []
        
        p=head
        while p:
            res.append(p.val)
            p= p.next

        for i in range(0,len(res)//2):
            sum_res.append(res[i]+res[-1-i])
        
        return max(sum_res)


        
# @lc code=end

