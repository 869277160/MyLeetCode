#
# @lc app=leetcode.cn id=328 lang=python3
#
# [328] 奇偶链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None:
            return None
        
        odd, eve = head, head.next  
        p1, p2 = odd, eve
        
        while(p1 != None and p2 != None):
            if p1.next is None or p2.next is None:
                break
            p1.next = p1.next.next
            p2.next = p2.next.next
            p1 = p1.next
            p2 = p2.next
        
        p1.next = eve 
        
        return odd
        
        
# @lc code=end

