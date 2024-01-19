'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-21 23:56:34
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-22 00:02:42
FilePath: \Leetcode_Solver\2357.使数组中所有元素都等于零.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2357 lang=python3
#
# [2357] 使数组中所有元素都等于零
#

# @lc code=start
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        
        if set(nums) == {0}:
            return 0
        else:
            
            count = 0
            while(set(nums) != {0}):
                min_num = min(nums, key=lambda x: x if x != 0 else float('inf'))
                nums = [num - min_num for num in nums if num != 0]
                count += 1
                # if 0 in nums :
                #     nums.remove(0)
                print(nums)
            
            return count 
        
        
        
# @lc code=end

