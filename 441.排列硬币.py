'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-15 22:25:18
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-17 18:43:09
FilePath: \Leetcode_Solver\441.排列硬币.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=441 lang=python3
#
# [441] 排列硬币
#

# @lc code=start
class Solution:
    def arrangeCoins(self, n: int) -> int:
        
        # # 1,3,6,10,15,21
        # import math 
        # for i in range(0,n+1):
        #     if i*(i+1)/2 >= n:
        #         if i*(i+1)/2 == n:
        #             return i
        #         else :
        #             count = 0
        #             temp_n = n
        #             for j in range(1,i+1):
        #                 temp_n -= j
        #                 count += 1
        #                 print(temp_n,count)
        #                 if temp_n <= 0 :
        #                     return count if temp_n == 0 else count - 1 
        c = 0 
        while n > c:
            c = c + 1
            n = n - c
        return c
                    
# @lc code=end

