'''
Author: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
Date: 2023-02-05 15:35:34
LastEditors: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
LastEditTime: 2023-02-05 15:42:04
FilePath: \Leetcode_Solver\172.阶乘后的零.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=172 lang=python3
#
# [172] 阶乘后的零
#

# @lc code=start
class Solution:
    # 实际上是转化为求5的个数
    # NOTE：注意这里的5的个数需要进一步考虑5的倍数的个数，比如25，125，625，3125，15625等等
    def trailingZeroes(self, n: int) -> int:
        res = 0
        for i in range(1, n+1):
            if i % 5  == 0 :
                res += 1 
            if i % 25 == 0:
                res += 1
            if i% 125 == 0:
                res += 1
            if i % 625 == 0:
                res += 1
            if i % 3125 == 0:
                res +=1 
            if i % 15625 == 0:
                res += 1
        return res 

# @lc code=end

