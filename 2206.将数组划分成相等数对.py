'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-17 09:50:21
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-17 09:51:05
FilePath: \Leetcode_Solver\2206.将数组划分成相等数对.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2206 lang=python3
#
# [2206] 将数组划分成相等数对
#

# @lc code=start
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        if len(nums) % 2 == 1:
            return False
        nums.sort()
        for i in range(0,len(nums),2):
            if nums[i] != nums[i+1]:
                return False
        return True
        
        
        
# @lc code=end

