#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None and list2 == None: return None 
        if list1 == None : return list2 
        if list2 == None : return list1 
        
        res = ListNode()
        res_p = res 
        
        p1, p2 = list1,list2
        
        while(p1 and p2):
            if p1.val > p2.val:
                    res_p.next = p2
                    p2 = p2.next
            else:
                    res_p.next = p1
                    p1 = p1.next
                    
            res_p = res_p.next
        
        
        if p1 == None: res_p.next = p2
        if p2 == None: res_p.next = p1
            
                
        return res.next
        
        
        
        
# @lc code=end

