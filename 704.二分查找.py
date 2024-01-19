'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-07 12:43:41
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-07 12:46:59
FilePath: \Leetcode_Solverd:\Leetcode_Solver\704.二分查找.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=704 lang=python3
#
# [704] 二分查找
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # if target not in nums:
        #     return -1
        # else:
        #     return nums.index(target)
        
        
        left, right = 0, len(nums) -1
        while(left <= right):
            mid = left + (right - left) //2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid -1 
            elif nums[mid] == target:
                return mid
        
        return -1 
        
        
# @lc code=end

