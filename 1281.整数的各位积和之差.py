'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-17 09:44:16
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-17 09:44:40
FilePath: \Leetcode_Solver\1281.整数的各位积和之差.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1281 lang=python3
#
# [1281] 整数的各位积和之差
#

# @lc code=start
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        
        product = 1
        sum = 0
        while n > 0:
            digit = n % 10
            product *= digit
            sum += digit
            n = n // 10
        
        return product - sum
        
# @lc code=end

