'''
Author: DingWang wangding19@mails.ucas.ac.cn
Date: 2024-01-30 14:29:59
LastEditors: DingWang wangding19@mails.ucas.ac.cn
LastEditTime: 2024-01-30 14:43:26
FilePath: \Leetcode_Solver\1019.链表中的下一个更大节点.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1019 lang=python3
#
# [1019] 链表中的下一个更大节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        stk = []
        n = len(nums)
        ans = [0] * n
        for i in range(n - 1, -1, -1):
            while stk and stk[-1] <= nums[i]:
                stk.pop()
            if stk:
                ans[i] = stk[-1]
            stk.append(nums[i])
        return ans

        
# @lc code=end

