'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-19 15:48:24
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-19 15:48:38
FilePath: \Leetcode_Solver\1903.字符串中的最大奇数.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1903 lang=python3
#
# [1903] 字符串中的最大奇数
#

# @lc code=start
class Solution:
    def largestOddNumber(self, num: str) -> str:
        
        
        for i in range(len(num)-1, -1, -1):
            if int(num[i]) % 2 == 1:
                return num[:i+1]
        
        return ""
# @lc code=end

