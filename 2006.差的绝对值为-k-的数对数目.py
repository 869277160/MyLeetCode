'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-20 14:59:52
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-20 15:01:02
FilePath: \Leetcode_Solver\2006.差的绝对值为-k-的数对数目.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2006 lang=python3
#
# [2006] 差的绝对值为 K 的数对数目
#

# @lc code=start
class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        
        res = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if abs(nums[i]-nums[j])==k:
                    res+=1
                    
        return res 
        
        
        
        
# @lc code=end

