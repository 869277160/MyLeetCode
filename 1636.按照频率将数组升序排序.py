'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-20 15:05:39
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-20 15:09:06
FilePath: \Leetcode_Solver\1636.按照频率将数组升序排序.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1636 lang=python3
#
# [1636] 按照频率将数组升序排序
#

# @lc code=start
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        import collections
        
        freq = collections.Counter(nums)
        
        nums.sort(key=lambda x: (freq[x], -x))
        
        return nums 
        
# @lc code=end

