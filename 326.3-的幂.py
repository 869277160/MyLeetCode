'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-17 10:31:46
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-17 10:32:17
FilePath: \Leetcode_Solver\326.3-的幂.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=326 lang=python3
#
# [326] 3 的幂
#

# @lc code=start
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        
        while n > 1:
            if n % 3 != 0:
                return False
            else:
                n = n // 3
                
        return n == 1
# @lc code=end

