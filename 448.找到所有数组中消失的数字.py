'''
Author: DingWang wangding19@mails.ucas.ac.cn
Date: 2024-01-28 17:06:15
LastEditors: DingWang wangding19@mails.ucas.ac.cn
LastEditTime: 2024-01-28 22:34:50
FilePath: \Leetcode_Solver\448.找到所有数组中消失的数字.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=448 lang=python3
#
# [448] 找到所有数组中消失的数字
#

# @lc code=start
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        from collections import Counter
        count = Counter(nums)
        res = []
        for i in range(1, len(nums)+1):
            if i not in count:
                res.append(i)
        return res
        
# @lc code=end

