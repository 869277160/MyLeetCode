#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        resHead = ListNode(-1)
        adder = 0
        
        p1,p2,pr = l1,l2,resHead
        
        while(p1!= None or p2 != None):
            if p1!= None and p2 != None:
                current_res = p1.val + p2.val + adder
                if current_res > 9:
                    current_res -= 10
                    adder = 1
                else:
                    adder = 0
                pr.next = ListNode(current_res)
                p1 = p1.next
                p2 = p2.next
                pr = pr.next
            
            if p1== None and p2 != None:
                current_res =  p2.val + adder
                if current_res > 9:
                    current_res -= 10
                    adder = 1
                else:
                    adder = 0
                pr.next = ListNode(current_res)
                p2 = p2.next
                pr = pr.next
                
                
            if p1!= None and p2 == None:
                current_res =  p1.val + adder
                if current_res > 9:
                    current_res -= 10
                    adder = 1
                else:
                    adder = 0
                pr.next = ListNode(current_res)
                p1 = p1.next
                pr = pr.next
                
                
        if adder != 0:
            pr.next = ListNode(1)
                
        return resHead.next
        
# @lc code=end

