'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-06 10:07:43
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-06 10:09:58
FilePath: \Leetcode_Solverd:\Leetcode_Solver\1630.等差子数组.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1630 lang=python3
#
# [1630] 等差子数组
#

# @lc code=start
class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        
        res = []
        for left,right, in zip(l,r):
            if self.checkList(sorted(nums[left:right+1])):
                res += [True]
            else:
                res += [False]
        
        return res 
    
    
    def checkList(self, input_list):
        
        dis = input_list[1] - input_list[0]
        for i in range(2, len(input_list)):
            if input_list[i] - input_list[i-1] != dis :
                return False
        
        return True 
        
        
        
# @lc code=end

