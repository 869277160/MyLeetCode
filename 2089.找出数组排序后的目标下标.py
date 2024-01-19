'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-21 10:50:37
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-21 10:52:47
FilePath: \Leetcode_Solver\2089.找出数组排序后的目标下标.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2089 lang=python3
#
# [2089] 找出数组排序后的目标下标
#

# @lc code=start
class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        
        return [] if target not in nums else [i for i in range(len(nums)) if sorted(nums)[i]==target]
        
        
        
# @lc code=end

