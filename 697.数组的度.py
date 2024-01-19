'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-08 09:16:11
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-16 22:08:48
FilePath: \Leetcode_Solver\697.数组的度.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=697 lang=python3
#
# [697] 数组的度
#

# @lc code=start
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        # 用字典进行解决
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if len(set(nums)) == len(nums):
            return 1
        
        max_count = 0 
        # min_len = 999
        res_dict = {}
        for i in range(len(nums)):
            if nums[i] not in res_dict.keys():
                res_dict[nums[i]] = [0,i,-1,1]
            res_dict[nums[i]][0] = res_dict[nums[i]][0] + 1
            res_dict[nums[i]][2] = i
            res_dict[nums[i]][3] = res_dict[nums[i]][2] - res_dict[nums[i]][1] +1
        
        
        min_len = min([res_dict[i][3] for i in res_dict.keys() if res_dict[i][0] == max([res_dict[i][0] for i in res_dict.keys()])])
        
        return min_len
# @lc code=end

