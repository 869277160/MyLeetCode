'''
Author: DingWang wangding19@mails.ucas.ac.cn
Date: 2024-01-23 15:43:47
LastEditors: DingWang wangding19@mails.ucas.ac.cn
LastEditTime: 2024-01-23 16:07:57
FilePath: \Leetcode_Solver\410.分割数组的最大值.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=410 lang=python3
#
# [410] 分割数组的最大值
#

# @lc code=start
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        # 确定搜索范围，
        # 最小值为当前数组中的最大值，最大值为整个数组的和
        min_idx = max(nums)
        max_idx = sum(nums)
        
        while min_idx < max_idx:
           
            mid_idx = min_idx + (max_idx - min_idx) // 2
            print(min_idx, mid_idx, max_idx)
            print(self.f(nums, mid_idx))
            if self.f(nums, mid_idx) > k:
                # 分割的多了，说明可以继续分，在 (mid_idx, max_idx] 中继续分割
                min_idx = mid_idx + 1 

            if self.f(nums, mid_idx) < k:
                # 分割的少了，说明不可以继续分，在 (min_idx, mid_idx] 中继续分割
                max_idx = mid_idx
            if self.f(nums, mid_idx) == k:
                max_idx = mid_idx
            print(min_idx, mid_idx, max_idx)
        return min_idx
    
    def f(self, nums: List[int], target_sum: int) -> int:
        
        current_sum = 0
        split_num = 1
        
        for num in nums:
            current_sum += num
            if current_sum > target_sum:
                split_num += 1 
                current_sum = num
        return split_num 
        
# @lc code=end

