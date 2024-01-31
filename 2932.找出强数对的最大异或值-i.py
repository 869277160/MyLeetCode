'''
Author: DingWang wangding19@mails.ucas.ac.cn
Date: 2024-01-29 15:54:06
LastEditors: DingWang wangding19@mails.ucas.ac.cn
LastEditTime: 2024-01-29 15:57:41
FilePath: \Leetcode_Solver\2932.找出强数对的最大异或值-i.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2932 lang=python3
#
# [2932] 找出强数对的最大异或值 I
#

# @lc code=start
class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        
        res = 0
        nums.sort()
        for i in range(len(nums)-1):
            for j in range(i, len(nums)):
                if nums[j] <= 2*nums[i]:
                    res = max(res, nums[i] ^ nums[j])
        return res
# @lc code=end

