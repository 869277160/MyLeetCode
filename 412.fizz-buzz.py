'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-17 18:14:04
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-17 18:14:52
FilePath: \Leetcode_Solver\412.fizz-buzz.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=412 lang=python3
#
# [412] Fizz Buzz
#

# @lc code=start
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        for i in range(1,n+1):
            if i % 3 == 0 and i % 5 == 0:
                res.append("FizzBuzz")
            elif i % 3 == 0:
                res.append("Fizz")
            elif i % 5 == 0:
                res.append("Buzz")
            else:
                res.append(str(i))
        return res
# @lc code=end

