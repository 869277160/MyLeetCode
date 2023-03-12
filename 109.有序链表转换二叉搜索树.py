'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-25 21:06:15
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-25 21:26:04
FilePath: \Leetcode_Solver\109.有序链表转换二叉搜索树.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=109 lang=python3
#
# [109] 有序链表转换二叉搜索树
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        
        if head == None:
            return None 
        elif head.next == None :
            return TreeNode(head.val)
        elif head.next.next == None :
            return TreeNode(head.next.val,left= TreeNode(head.val))
        else :
            fast, slow = head, head 
            dummy = ListNode(0,head)
            slow_before = dummy
            while(fast != None):
                if fast.next == None:
                    slow_val = slow.val
                    root = TreeNode(slow_val)
                    root.right = self.sortedListToBST(slow.next)
                    slow_before.next = None 
                    root.left = self.sortedListToBST(head)
                    return root
                    # slow = slow.next
                    # break
                
                else:
                    fast = fast.next.next 
                
                slow = slow.next
                slow_before = slow_before.next

            root = TreeNode(slow.val)
            root.right = self.sortedListToBST(slow.next)
            slow_before.next = None 
            root.left = self.sortedListToBST(head)
            return root 
        
        
        
        
# @lc code=end

