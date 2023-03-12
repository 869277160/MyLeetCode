'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-01 09:45:02
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-01 09:45:35
FilePath: \Leetcode_Solver\1295.统计位数为偶数的数字.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1295 lang=python3
#
# [1295] 统计位数为偶数的数字
#

# @lc code=start
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        
        res = 0
        for i in nums:
            if len(str(i)) % 2 == 0:
                res += 1
        return res
    
# @lc code=end

