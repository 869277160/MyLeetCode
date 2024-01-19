'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-12 15:14:53
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-12 15:25:00
FilePath: \Leetcode_Solver\410.分割数组的最大值.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=410 lang=python3
#
# [410] 分割数组的最大值
#

# @lc code=start
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        
        if k == len(nums):
            return max(nums)
        if k == 1 :
            return sum(nums)
        else : 
            
            # 线性搜索各个最大值是否可以对数组进行分割
            for total in range(max(nums),sum(nums)+1):
                if self.SplitList(nums, total) <= k:
                    return total
            
                
                # # 二分搜索各个最大值是否可以对数组进行分割
                # min_sum, max_sum = max(nums), sum(nums)+1
                # while(min_sum < max_sum):
                #     mid_sum = min_sum + (max_sum-min_sum ) // 2
                #     if self.SplitList(nums, mid_sum) <= k:
                #         max_sum = mid_sum
                #     else :
                #         min_sum = mid_sum +1
                # return min_sum
        
    
    def SplitList(self, nums, max):
        count = 1
        sum = 0
        for num in nums:
            if sum + num > max:
                count +=1 
                sum = num
            else:
                sum += num
            
        return count 


# @lc code=end

