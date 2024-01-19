'''
Author: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
Date: 2023-02-06 10:16:31
LastEditors: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
LastEditTime: 2023-02-06 10:18:37
FilePath: \Leetcode_Solver\349.两个数组的交集.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=349 lang=python3
#
# [349] 两个数组的交集
#

# @lc code=start
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        set1 = [0]*2000
        set2 = [0]*2000
        output = []
        
        for i in nums1:
            set1[i] = True
        for i in nums2:
            set2[i] = True
        
        for i in range(1003):
            if set1[i] and set2[i]:
                output.append(i)

        return output
                
                
# @lc code=end

