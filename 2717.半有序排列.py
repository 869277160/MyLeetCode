'''
Author: DingWang wangding19@mails.ucas.ac.cn
Date: 2024-01-29 20:11:09
LastEditors: DingWang wangding19@mails.ucas.ac.cn
LastEditTime: 2024-01-29 20:18:47
FilePath: \Leetcode_Solver\2717.半有序排列.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2717 lang=python3
#
# [2717] 半有序排列
#

# @lc code=start
class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        length = len(nums)

        idx_1 = nums.index(1)
        idx_n = nums.index(length)
        
        if idx_1 > idx_n :
            return idx_1 + length -1 - idx_n -1
        else:
            return idx_1 + length -1 - idx_n
            
      
        
        
# @lc code=end

