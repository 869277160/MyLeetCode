'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-16 23:51:29
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-16 23:53:26
FilePath: \Leetcode_Solver\2176.统计数组中相等且可以被整除的数对.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2176 lang=python3
#
# [2176] 统计数组中相等且可以被整除的数对
#

# @lc code=start
class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        
        if len(set(nums)) == len(nums):
            return 0
        
        res = 0
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j] and i*j % k == 0:
                    res +=1 
                   
        return res 
        
# @lc code=end

