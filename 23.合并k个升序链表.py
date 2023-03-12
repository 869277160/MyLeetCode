#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并K个升序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        if lists == [] or lists == [[]]:
            return None 
        if len(lists) == 1:
            return lists[0]

        else :
            while len(lists) > 1:
                lists.append(self.merge2Lists(lists[0],lists[1]))
                if len(lists) == 3: return lists[-1]
                else:
                    lists = lists[2:]
                
    
    def merge2Lists(self,list1,list2):
        if list1 == None :
            return  list2 
        if list2 == None :
            return list1 
        
        res = ListNode(-1)
        p_res = res
        p1, p2 = list1, list2
        
        while(p1 or p2):
           
            if p1 == None and p2 == None :
                return res.next 
            
            if p1 == None and p2 != None :
                    p_res.next = p2
                    p2 = p2.next
                    
            if p1 != None and p2 == None :
                    p_res.next = p1
                    p1 = p1.next
                    
            if p1 != None and p2 != None :
                if p1.val < p2.val :
                    p_res.next = p1
                    p1 = p1.next 
                else :
                    p_res.next = p2
                    p2 = p2.next
            
            p_res = p_res.next
        
        return res.next
        
    
        
# @lc code=end

