'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-27 21:58:45
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-27 21:59:28
FilePath: \Leetcode_Solver\1512.好数对的数目.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1512 lang=python3
#
# [1512] 好数对的数目
#

# @lc code=start
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    res += 1
        return res

# @lc code=end

