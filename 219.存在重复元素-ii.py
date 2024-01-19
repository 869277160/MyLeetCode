'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-19 15:22:34
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-19 15:34:57
FilePath: \Leetcode_Solver\219.存在重复元素-ii.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=219 lang=python3
#
# [219] 存在重复元素 II
#

# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        nums_dict = {}
        
        for i in range(len(nums)):
            if nums[i] not in nums_dict.keys():
                nums_dict[nums[i]] = [i]
            else:
                nums_dict[nums[i]].append(i)
        
        
        for key in nums_dict.keys():
            if len(nums_dict[key]) > 1:
                for i in range(len(nums_dict[key])-1):
                    if nums_dict[key][i+1] - nums_dict[key][i] <= k:
                        return True
        
        
        
        # for i in range(len(nums)):
        #     if i+k >= len(nums):
        #         if nums[i] in nums[i+1:]:
        #             return True
        #     if i+k < len(nums):
        #         if nums[i] in nums[i+1:i+k+1]:
        #             return True
        #     if i-k >= 0:
        #         if nums[i] in nums[i-k:i]:
        #             return True
        #     if i-k < 0:
        #         if nums[i] in nums[:i]:
        #             return True
        #         # if nums[i] == nums[j] and abs(i-j) <= k:
        #         #     return True

        return False 
        
# @lc code=end

