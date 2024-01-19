'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-21 09:44:24
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-21 09:54:33
FilePath: \Leetcode_Solver\1752.检查数组是否经排序和轮转得到.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1752 lang=python3
#
# [1752] 检查数组是否经排序和轮转得到
#

# @lc code=start
class Solution:
    def check(self, nums: List[int]) -> bool:
        
        #  1、暴力法
        # for i in range(len(nums)):
        #     print(nums[i:],nums[:i])
        #     if self.checker(nums[i:]) and self.checker(nums[:i]):
        #         if i == 0 :
        #             return True
        #         else :
        #             if nums[-1] <= nums[0]:
        #                 return True
            
        # return False
        
        # 2、目标匹配
        target = sorted(nums)
        temp = nums + nums
        
        for i in range(len(nums)):
            if temp[i] == target[0]:
                if temp[i:i+len(nums)] == target:
                    return True
        return False        
    
    def checker(self, input_list):
        for i in range(len(input_list)-1):
            if input_list[i] > input_list[i+1]:
                return False
        return True 
        
        
        
# @lc code=end

