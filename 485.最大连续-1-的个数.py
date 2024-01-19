'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-20 21:39:02
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-20 21:42:58
FilePath: \Leetcode_Solver\485.最大连续-1-的个数.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=485 lang=python3
#
# [485] 最大连续 1 的个数
#

# @lc code=start
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # num_str = ''.join([str(i) for i in nums])
        # return max([len(i) for i in num_str.split('0')])
        res = [0 for i in range(len(nums))]
        
        last = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                res[i] = last + 1
                last = res[i]
        
        return max(res)
        
                
        
# @lc code=end

