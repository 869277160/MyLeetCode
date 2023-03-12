'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-21 10:50:14
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-21 10:54:23
FilePath: \Leetcode_Solver\2164.对奇偶下标分别排序.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2164 lang=python3
#
# [2164] 对奇偶下标分别排序
#

# @lc code=start
class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        if len(nums)< 2 :
            return nums 
        
        eve = sorted([nums[i] for i in range(0,len(nums),2)])
        odd = sorted([nums[i] for i in range(1,len(nums),2)],reverse=True)
        
        for i in range(len(nums)):
            nums[i] = eve[i//2] if i % 2 == 0 else odd[i//2] 
        
        return nums
        
                
# @lc code=end

