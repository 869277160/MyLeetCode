'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-16 22:11:05
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-16 22:15:55
FilePath: \Leetcode_Solver\1018.可被-5-整除的二进制前缀.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1018 lang=python3
#
# [1018] 可被 5 整除的二进制前缀
#

# @lc code=start
class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        res = []
        pre = 0
        for i in nums:
            pre = ((pre<<1)+i)%5
            res.append(not pre)
        return res

# @lc code=end

