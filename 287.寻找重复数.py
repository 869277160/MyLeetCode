'''
Author: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
Date: 2023-02-07 10:06:23
LastEditors: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
LastEditTime: 2023-02-07 10:10:39
FilePath: \Leetcode_Solver\287.寻找重复数.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=287 lang=python3
#
# [287] 寻找重复数
#

# @lc code=start
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
      for i in range(len(nums)):
          for j in range(i+1,len(nums)):
              if nums[i] == nums[j]:
                  return nums[i]
                
        
# @lc code=end

