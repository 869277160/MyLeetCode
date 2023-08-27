'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-17 17:14:58
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-17 17:29:07
FilePath: \Leetcode_Solver\35.搜索插入位置.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        if target >= nums[-1]:
            return len(nums)-1 if target == nums[-1] else len(nums)
        elif target <= nums[0]:
            return 0
        elif target < nums[-1] and target > nums[0]:
            # 二分搜索
            left, right = 0, len(nums)
            while(left < right):
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    return mid 
                elif nums[mid] < target:
                    left = mid + 1 
                elif nums[mid] > target:
                    right = mid 
                # print(mid,left,right)
            
            
            return left 
# @lc code=end

