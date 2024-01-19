'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-24 09:55:41
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-24 09:59:18
FilePath: \Leetcode_Solver\303.区域和检索-数组不可变.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=303 lang=python3
#
# [303] 区域和检索 - 数组不可变
#

# @lc code=start
class NumArray:

    def __init__(self, nums: List[int]):
        # self.array = nums
        
        self.preSum = [0] * (len(nums) + 1)
        for i in range(1, len(self.preSum)):
            self.preSum[i] = self.preSum[i - 1] + nums[i - 1]
    
    def sumRange(self, left: int, right: int) -> int:
        # return sum(self.array[left:right+1])

        return self.preSum[right+1] - self.preSum[left]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
# @lc code=end

