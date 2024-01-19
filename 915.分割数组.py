'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-17 00:16:19
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-17 00:16:53
FilePath: \Leetcode_Solver\915.分割数组.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=915 lang=python3
#
# [915] 分割数组
#

# @lc code=start
class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        
        n = len(nums)
        minv = [0] * (n + 10)
        minv[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            minv[i] = min(minv[i + 1], nums[i])
        maxv = 0
        for i in range(n - 1):
            maxv = max(maxv, nums[i])
            if maxv <= minv[i + 1]:
                return i + 1
        return -1


# @lc code=end

