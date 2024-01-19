'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-22 10:06:06
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-22 10:09:00
FilePath: \Leetcode_Solver\922.按奇偶排序数组-ii.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=922 lang=python3
#
# [922] 按奇偶排序数组 II
#

# @lc code=start
class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        
        odd, eve =1,0
        
        res = [0] * len(nums)
        
        for i in nums:
            if i % 2 == 1:
                res[odd] = i
                odd += 2
            if i % 2 == 0:
                res[eve] = i
                eve += 2
            # else:
            #     res.append(nums[odd])
            #     res.append(nums[eve])
            #     odd += 2
            #     eve += 2
        
        return res 
        
        
# @lc code=end

