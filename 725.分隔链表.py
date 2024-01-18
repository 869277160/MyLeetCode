'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-08-28 10:22:20
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-08-28 11:08:15
FilePath: \Leetcode_Solver\725.分隔链表.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=725 lang=python3
#
# [725] 分隔链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        # # print(head)
        # if head==None:
        #     return []
        # elif k == 0:
        #     return []
        # elif k == 1:
        #     return [head]
        
        
        # res = [None for _ in range(k)]
        # res[0] = head
        # # 初始化指针数组，按顺序指向前k个结点
        # for i in range(1, k):
        #     if res[i - 1]:
        #         res[i] = res[i - 1].next
        # # 移动指针，数组下标为 i 的指针每次前进 i + 1
        # while res[k - 1]:
        #     for i in range(k-1):
        #         res[k - 1] = res[k - 1].next
        #         if not res[k - 1]:
        #             break
        #         for j in range(i, k - 1):
        #             res[j] = res[j].next
        #     if res[k - 1]:
        #         res[k - 1] = res[k - 1].next
        # # 此时链表已经由 k - 1 个指针划分为 k 段，数组中的指针均指向各段最后一个结点
        # # 将链表分割成 k 段，并将数组指针设为各段的头结点, 即上一段最后一个结点的next指针指向的结点
        # for i in range(k - 1, 0, -1):
        #     if res[i - 1]:
        #         res[i] = res[i - 1].next
        #         res[i - 1].next = None
        # # 第一段的头结点为 root
        # res[0] = head


        
        # return res 
            

        n = 0
        node = head
        while node:
            n += 1
            node = node.next
        quotient, remainder = n // k, n % k

        parts = [None for _ in range(k)]
        i, curr = 0, head
        while i < k and curr:
            parts[i] = curr
            part_size = quotient + (1 if i < remainder else 0)
            for _ in range(part_size - 1):
                curr = curr.next
            next = curr.next
            curr.next = None
            curr = next
            i += 1
        return parts

        
        
                
        
# @lc code=end

