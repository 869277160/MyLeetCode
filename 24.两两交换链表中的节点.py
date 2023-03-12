#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head == None :
            return head 
        elif head.next == None:
            return head
        elif head.next.next == None:
            temp = head.next
            head.next.next = head
            head.next = None 
            
            return temp 
        else :
            # swap the head and the second node for return 
            temp = head.next
            head.next = temp.next
            temp.next = head 

            p = head
            
            while(p):
                # 奇数个节点
                if p.next == None:
                    return temp
                elif p.next.next == None :
                    return temp 
                else:
                    # swap the p and the p.next
                    temper = p.next 
                    temper2 = p.next.next
                    
                    temper.next = temper2.next 
                    temper2.next = temper
                    p.next = temper2
                    
                    
                    p = p.next.next 
                    
            return temp 
        
# @lc code=end

