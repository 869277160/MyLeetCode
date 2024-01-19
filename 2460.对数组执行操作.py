'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-22 10:13:26
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-22 10:24:26
FilePath: \Leetcode_Solver\2460.对数组执行操作.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2460 lang=python3
#
# [2460] 对数组执行操作
#

# @lc code=start
class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        
        new_nums = []
        
        pos = 0
        zeros = 0
        while(pos<len(nums)-1):
            if nums[pos] == nums[pos+1] and nums[pos] != 0:
                nums[pos] = nums[pos]*2
                nums[pos+1] = 0
                
                new_nums.append(nums[pos])
                # pos += 1
                # zeros += 1
            else:
                if nums[pos] == 0:
                    zeros += 1
                else:
                    new_nums.append(nums[pos])
                    
            
            pos += 1
            print(new_nums)
            
        
        new_nums.append(nums[-1])
        new_nums += [0 for i in range(zeros)]
        
        return new_nums
        
        
        
        
# @lc code=end

