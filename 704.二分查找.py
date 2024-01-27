'''
Author: DingWang wangding19@mails.ucas.ac.cn
Date: 2024-01-23 12:57:16
LastEditors: DingWang wangding19@mails.ucas.ac.cn
LastEditTime: 2024-01-23 13:15:57
FilePath: \Leetcode_Solver\704.二分查找.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=704 lang=python3
#
# [704] 二分查找
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0 , len(nums) - 1 
        
        while left <= right :
            mid = left + (right - left) // 2
            # print(left, right)
            if nums[mid] < target:
                left = mid + 1 
            elif nums[mid] > target:
                right = mid -1 
            elif nums[mid] == target:
                return mid 
        
        return -1 












# @lc code=end

