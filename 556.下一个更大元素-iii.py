'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-26 10:54:14
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-26 11:20:47
FilePath: \Leetcode_Solver\556.下一个更大元素-iii.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=556 lang=python3
#
# [556] 下一个更大元素 III
#

# @lc code=start
class Solution:
    def nextGreaterElement(self, n: int) -> int:

        if n <= 10:
            return -1
        if n == 2**31-1: 
            return -1
        else:
            res = -1
            nums = [int(i) for i in str(n)]
            for i in range(len(nums)-1,-1,-1):
                if (nums[i] > nums[i-1]):
                    nums[i:] = sorted(nums[i:])
                    for j in range(i,len(nums)):
                        if nums[j] > nums[i-1]:
                            t = nums[i-1]
                            nums[i-1] = nums[j]
                            nums[j] = t
                            
                            res = int(''.join([str(i) for i in nums]))

                            # 判断是否为合法整数
                            if res <= 2**31-1 and res >= -2**31:
                                return res
                            else :
                                return -1
        
        
            return -1 
# @lc code=end

