'''
Author: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
Date: 2023-02-07 09:28:22
LastEditors: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
LastEditTime: 2023-02-07 09:57:47
FilePath: \Leetcode_Solver\13.罗马数字转整数.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#

# @lc code=start
class Solution:
    # 把特殊情况视为两个为一组进行判断即可
    # 结尾肯定会有单独一个字符或者没有字符
    def romanToInt(self, s: str) -> int:
        
        elem = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000,}
        # order = ["I","V","X","L","C","D","M",]
        wrong_order_elem = {"IV":4,"IX":9,"XL":40,"XC":90,"CD":400,"CM":900,}
        
        # for i in range(0,len(s)):
        output = 0
        i = 0
        while(i < len(s)):
            if s[i:i+2] in wrong_order_elem.keys():
                output += wrong_order_elem[s[i:i+2]]
                i += 2 
            else:
                output += elem[s[i:i+1]]
                i += 1 
        
        return output
        
        
        
# @lc code=end

