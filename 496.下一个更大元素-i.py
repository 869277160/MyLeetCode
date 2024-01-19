'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-26 10:23:54
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-26 10:52:12
FilePath: \Leetcode_Solver\496.下一个更大元素-i.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=496 lang=python3
#
# [496] 下一个更大元素 I
#

# @lc code=start
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        res = {}
        for i in range(len(nums2)):
            res[nums2[i]] = -1
        stack = []
        for i in range(len(nums2)-1,-1,-1):
            while(len(stack)>0 and stack[-1] <= nums2[i]):
                stack.pop()
         
            res[nums2[i]] = stack[-1] if len(stack) > 0 else -1
            stack.append(nums2[i])
        
        all_res = [res[i] for i in nums1]
        
        
        return all_res
        
# @lc code=end

