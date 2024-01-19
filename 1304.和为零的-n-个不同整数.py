'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-21 23:00:59
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-21 23:01:50
FilePath: \Leetcode_Solver\1304.和为零的-n-个不同整数.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1304 lang=python3
#
# [1304] 和为零的 N 个不同整数
#

# @lc code=start
class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n == 1:
            return [0]
        else :
            if n % 2 ==0:
                return [i for i in range(1, n//2+1)] + [-i for i in range(1, n//2+1)]
            else :
                return [i for i in range(1, n//2+1)] + [-i for i in range(1, n//2+1)] + [0]
            
# @lc code=end

