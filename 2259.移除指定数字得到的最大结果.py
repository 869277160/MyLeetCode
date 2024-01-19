'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-23 09:16:05
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-23 09:21:33
FilePath: \Leetcode_Solver\2259.移除指定数字得到的最大结果.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2259 lang=python3
#
# [2259] 移除指定数字得到的最大结果
#

# @lc code=start
class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        
        # 暴力求解
        res = [ ]
        for i in range(len(number)):
            if number[i] == digit:
                res.append(number[:i] + number[i+1:])
        
        return max(res)

        # 优化，推理一下删除位置的规律
        # 如果数字是递增的，那么直接删除最后一个数字即可
        
# @lc code=end

