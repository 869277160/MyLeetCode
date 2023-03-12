'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-16 22:07:33
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-16 22:12:07
FilePath: \Leetcode_Solver\504.七进制数.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=504 lang=python3
#
# [504] 七进制数
#

# @lc code=start
class Solution:
    def convertToBase7(self, num: int) -> str:
        
        if num > 0:
            res = ""
            while num:
                res = "{}".format(num%7) + res 
                num //= 7
            return res 
        elif num <0:
            res = ""
            num = -num
            while num:
                res = "{}".format(num%7) + res 
                num //= 7
            return "-"+res 
        else:
            return "0"
# @lc code=end

