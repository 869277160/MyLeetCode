'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-18 16:12:50
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-18 16:24:35
FilePath: \Leetcode_Solver\2469.温度转换.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2469 lang=python3
#
# [2469] 温度转换
#

# @lc code=start
class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        
        
        res1 = "{:.5f}".format(celsius + 273.15)
        res2 = "{:.5f}".format(celsius * 1.8 + 32)
        
        return [float(res1) ,float(res2)  ]
        
# @lc code=end

