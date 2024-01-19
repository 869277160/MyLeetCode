'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-24 09:49:35
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-24 09:54:27
FilePath: \Leetcode_Solver\228.汇总区间.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=228 lang=python3
#
# [228] 汇总区间
#

# @lc code=start
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        
        if nums == []:
            return []
        
        current_begin = nums[0]
        current_end = nums[0]
        
        res = []
        for i in range(1,len(nums)):
            if nums[i] == current_end + 1:
                current_end = nums[i]
            else :
                if current_end == current_begin:
                    res.append(str(current_begin))
                else:
                    res.append(str(current_begin) + "->" + str(current_end))
            
                current_begin = nums[i]
                current_end = nums[i]
        
        if current_end == current_begin:
            res.append(str(current_begin))
        else:
            res.append(str(current_begin) + "->" + str(current_end))
        
        
        return res 
        
# @lc code=end

