'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-20 21:46:44
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-20 21:50:10
FilePath: \Leetcode_Solver\2553.分割数组中数字的数位.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2553 lang=python3
#
# [2553] 分割数组中数字的数位
#

# @lc code=start
class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        if all([i<10  for i in nums]):
            return nums
        else :
            res = []
            for i in range(len(nums)):
                if nums[i] <10 :
                    res += [nums[i]]
                else:
                    res += [int(j) for j in str(nums[i])]
            return res

# @lc code=end

