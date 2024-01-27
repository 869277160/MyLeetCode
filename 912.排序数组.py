'''
Author: DingWang wangding19@mails.ucas.ac.cn
Date: 2024-01-24 17:27:49
LastEditors: DingWang wangding19@mails.ucas.ac.cn
LastEditTime: 2024-01-24 17:41:06
FilePath: \Leetcode_Solver\912.排序数组.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=912 lang=python3
#
# [912] 排序数组
#

# @lc code=start
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        # solver 1
        # nums.sort()
        # return nums
        
        # solver 2 
        # self.quicksort(nums, 0, len(nums)-1)
        quick_sort(nums, 0, len(nums)-1)
        return nums
    
    
    def quicksort(self, nums: List[int], left: int, right:int):
        if left < right:
            pos = self.partition(nums, left, right)
            self.quicksort(nums, left, pos - 1)
            self.quicksort(nums, pos + 1, right)
    
    def partition(self, nums: List[int], left: int, right:int):
        # 找到开头元素的位置
        pivot = nums[left]
        
        while left < right:
            while left < right and nums[right] >= pivot: #
                right -= 1 
            nums[left] = nums[right];

            while left < right and nums[left] <= pivot:
                left += 1
            nums[right] = nums[left];

        nums[left] = pivot

        return left
