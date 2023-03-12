'''
Author: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
Date: 2023-02-05 15:01:07
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-15 16:18:14
FilePath: \Leetcode_Solver\70.爬楼梯.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        res = [i for i in range(n+1)]
        for i in range(3,n+1):
            res[i] = res[i-1] + res[i-2]
        return res[n]
    # self.climbStairs(n-1) + self.climbStairs(n-2)


# @lc code=end