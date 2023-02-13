'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-13 09:01:52
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-13 09:09:46
FilePath: \Leetcode_Solver\9.回文数.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # solver 1 
        # if x < 0:
        #     return False
        # else:
        #     return str(x) == str(x)[::-1]
        
        # solver 2 
        if x < 0:
            return False 
        else :
            return self.Int2list(x) == self.Int2list(x)[::-1]

    def Int2list(self,x):
        res = []
        while(x > 0) :
            res.append(x % 10)
            x = x // 10
        return res

# @lc code=end

