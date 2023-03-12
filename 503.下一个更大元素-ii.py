'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-26 10:51:55
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-26 10:53:35
FilePath: \Leetcode_Solver\503.下一个更大元素-ii.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=503 lang=python3
#
# [503] 下一个更大元素 II
#

# @lc code=start
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        length = len(nums)
        nums = nums + nums
        res = [0 for _ in nums]
        stack = []
        # index_stack = []
        for i in range(len(nums)-1,-1,-1):
            while(stack != [] and stack[-1] <= nums[i]):
                # stack.pop()
                stack.pop()
            
            res[i] = stack[-1] if stack != [] else -1
            stack.append(nums[i])
            # res[i] = index_stack[-1] - i if index_stack != [] else 0
            # index_stack.append(i)
        
        return res[:length]
        
        
        
# @lc code=end

