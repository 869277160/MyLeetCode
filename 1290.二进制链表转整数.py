#
# @lc app=leetcode.cn id=1290 lang=python3
#
# [1290] 二进制链表转整数
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        if head == None :
            return 
        
        if head.next == None:
            return head.val 
        
        if head.next.next == None:
            return head.val * 2 + head.next.val
        
        res_list = []
        p = head 
        while p:
            res_list.append(p.val)
            p=p.next
        
        # res_list = res_list[::-1]
        res = 0
        for i in range(len(res_list)):
            res += 2**(len(res_list)-1 - i) * res_list[i]
        return res 
            
        
        
# @lc code=end

