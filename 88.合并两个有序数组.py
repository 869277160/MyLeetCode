'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-10 10:12:06
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-10 14:57:21
FilePath: \Leetcode_Solver\88.合并两个有序数组.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        # 直接返回
        if m == 0:
            nums1 = nums2
            return 
        if n == 0:
            return

        
        # 双指针
        p1, p2 = 0,0
        
        while(p1<(m+n) and p2 < n):
            
            if p2 == n-1:
                return 
            
            if nums1[p1] >= nums2[p2]:
                # p1 += 1
                temp = nums1[p1]
                nums1[p1] = nums2[p2]
                nums1[p1+1] = temp
                nums1[p1+1:] = nums1[p1+1:-1]
                
                # p1 += 1
                p2 +=  1
                
                
            if nums1[p1] < nums2[p2] or p2 == n:
                p1 += 1
        
        return
# @lc code=end

