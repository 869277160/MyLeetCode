'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-16 23:40:55
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-16 23:41:52
FilePath: \Leetcode_Solver\2016.增量元素之间的最大差值.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2016 lang=python3
#
# [2016] 增量元素之间的最大差值
#

# @lc code=start
class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        
        res = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[j] - nums[i] > 0:
                    res.append(nums[j]-nums[i])
        
        return max(res) if res else -1 
        
        
        
# @lc code=end

