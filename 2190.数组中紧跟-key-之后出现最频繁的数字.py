'''
Author: DingWang wangding19@mails.ucas.ac.cn
Date: 2024-01-29 00:07:42
LastEditors: DingWang wangding19@mails.ucas.ac.cn
LastEditTime: 2024-01-29 00:11:40
FilePath: \Leetcode_Solver\2190.数组中紧跟-key-之后出现最频繁的数字.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2190 lang=python3
#
# [2190] 数组中紧跟 key 之后出现最频繁的数字
#

# @lc code=start
class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        count = []
        for i in range(len(nums)-1):
            if nums[i] == key:
                count.append(nums[i+1])
        from collections import Counter
        return Counter(count).most_common(1)[0][0]
        
        
        
        
        
# @lc code=end

