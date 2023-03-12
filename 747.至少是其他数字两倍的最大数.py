'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-17 10:34:51
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-17 10:36:13
FilePath: \Leetcode_Solver\747.至少是其他数字两倍的最大数.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=747 lang=python3
#
# [747] 至少是其他数字两倍的最大数
#

# @lc code=start
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        maxnum = max(nums)
        for i in range((maxnum//2)+1,maxnum):
            if i in nums :
                return -1 
        
        return nums.index(maxnum)
        
        
        
        
        
        
        
        
        
        
        
        
# @lc code=end

