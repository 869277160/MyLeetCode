'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-20 16:08:42
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-20 16:14:58
FilePath: \Leetcode_Solver\1827.最少操作使数组递增.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1827 lang=python3
#
# [1827] 最少操作使数组递增
#

# @lc code=start
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        ans=0
        for i in range(1,len(nums)):
            ans+=max(0,nums[i-1]+1-nums[i])
            nums[i]=max(nums[i],nums[i-1]+1)
        return ans
        
# @lc code=end

