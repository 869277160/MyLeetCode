'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-21 10:21:55
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-21 10:32:13
FilePath: \Leetcode_Solver\1758.生成交替二进制字符串的最少操作数.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1758 lang=python3
#
# [1758] 生成交替二进制字符串的最少操作数
#

# @lc code=start
class Solution:
    def minOperations(self, s: str) -> int:
        
        if len(s) == 1 :
            return 0
        elif len(s) == 2:
            if s == "01" or s == "10":
                return 0
            else :
                return 1
        else :
            res_str_1 = ""
            res_str_2 = ""
            if len(s) % 2 == 0:
                res_str_1 = "01" * (len(s)//2)
                res_str_2 = "10" * (len(s)//2)

            else :
                res_str_1 = "01" * (len(s)//2) + "0"
                res_str_2 = "10" * (len(s)//2) + "1"

            # path_1 = int(res_str_1,2) ^ int(s,2)
            # path_2 = int(res_str_2,2) ^ int(s,2)
                        
            path_1 = sum([1 for i in range(len(s)) if s[i] != res_str_1[i]])
            path_2 = sum([1 for i in range(len(s)) if s[i] != res_str_2[i]])
            

            return min(path_1,path_2)
        
        
        
# @lc code=end

