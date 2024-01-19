'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-21 10:53:48
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-21 11:00:30
FilePath: \Leetcode_Solver\2099.找到和最大的长度为-k-的子序列.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2099 lang=python3
#
# [2099] 找到和最大的长度为 K 的子序列
#

# @lc code=start
class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return [max(nums)]
        if k == len(nums):
            return nums 
        # order_dict = {nums[i]:i for i in range(len(nums))}
        res_list = sorted(nums)[-k:]

        res = []
        for i in range(len(nums)):
            if nums[i] in res_list:
                res.append(nums[i])
                res_list.remove(nums[i])
            if len(res) == k:
                break
        
        return res 
        
# @lc code=end

