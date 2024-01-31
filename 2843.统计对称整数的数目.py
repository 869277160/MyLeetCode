'''
Author: DingWang wangding19@mails.ucas.ac.cn
Date: 2024-01-29 19:00:15
LastEditors: DingWang wangding19@mails.ucas.ac.cn
LastEditTime: 2024-01-29 19:07:26
FilePath: \Leetcode_Solver\2843.统计对称整数的数目.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2843 lang=python3
#
# [2843] 统计对称整数的数目
#

# @lc code=start
class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        
        res = 0 
        for i in range(low,high+1):
            if len(str(i)) == 4:
                if int(str(i)[0]) + int(str(i)[1]) == int(str(i)[2]) + int(str(i)[3])  :
                    res+=1
            if len(str(i)) == 2:
                if str(i)[0] == str(i)[1]:
                    res+=1
        
        return res 
        
        
        
# @lc code=end

