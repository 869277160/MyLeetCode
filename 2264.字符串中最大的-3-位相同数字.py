'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-17 00:00:35
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-17 00:03:45
FilePath: \Leetcode_Solver\2264.字符串中最大的-3-位相同数字.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2264 lang=python3
#
# [2264] 字符串中最大的 3 位相同数字
#

# @lc code=start
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        
        res = []
        for i in range(len(num)-2):
            if num[i] == num[i+1] and num[i] == num[i+2]:
                # res.append(111*int(num[i]))
                res.append(num[i:i+3])
            i = i + 1
        return str(max(res)) if res else ''
        
        
        
# @lc code=end

