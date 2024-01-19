'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-13 17:04:03
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-13 17:08:30
FilePath: \Leetcode_Solver\263.丑数.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=263 lang=python3
#
# [263] 丑数
#

# @lc code=start
class Solution:
    def isUgly(self, n: int) -> bool:
        if n == 0 :
            return False
        if n ==1:
            return True
        else:
            while(n != 0):
                if n % 2 == 0:
                    n = n / 2
                if n % 3 == 0:
                    n = n / 3
                if n % 5 == 0:
                    n = n / 5
                if n == 1:
                    return True
                if n != 1 and n % 2 != 0 and n % 3 != 0 and n % 5 != 0:
                    return False
        
        
        
# @lc code=end

