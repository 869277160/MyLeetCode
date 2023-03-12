'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-18 11:45:44
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-18 11:49:09
FilePath: \Leetcode_Solver\2465.不同的平均值数目.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2465 lang=python3
#
# [2465] 不同的平均值数目
#

# @lc code=start
class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        
        avg_dict = {}
        
        while nums!=[]:
            avg = (max(nums)+min(nums))/2
            
            nums.remove(max(nums))
            nums.remove(min(nums))
            
            if avg in avg_dict.keys():
                avg_dict[avg] += 1
            else :
                avg_dict[avg] = 1
        
        return len(avg_dict.keys())
        
            
        
        
        
        
        
# @lc code=end

