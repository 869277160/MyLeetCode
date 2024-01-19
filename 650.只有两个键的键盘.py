'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-04-07 16:19:51
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-04-07 16:33:35
FilePath: \Leetcode_Solver\650.只有两个键的键盘.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=650 lang=python3
#
# [650] 只有两个键的键盘
#

# @lc code=start
class Solution:
    def minSteps(self, n: int) -> int:
        
        # memo = [0,0,2,3,4,5,5,7,6,6] + [-1 for i in range(10,n+1)]

        f = [0] * (n + 1)
        for i in range(2, n + 1):
            f[i] = 0xFFFFFFFF
            j = 1
            while j * j <= i:
                if i % j == 0:
                    f[i] = min(f[i], f[j] + i // j)
                    f[i] = min(f[i], f[i // j] + j)
                j += 1
                
        return f[n]
        
# @lc code=end

