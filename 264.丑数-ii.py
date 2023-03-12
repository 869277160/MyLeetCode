'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-13 17:08:51
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-13 17:12:08
FilePath: \Leetcode_Solver\264.丑数-ii.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=264 lang=python3
#
# [264] 丑数 II
#

# @lc code=start
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # res = [1, 2, 3, 4, 5, 6, 8, 9, 10, 12]
        
        # if n <= 10 :
        #     return res[n-1]
        # else:
        #     for i in range(10,n):
        #         res.append(res[i-1]+1)
        #         while res[i] % 2 != 0 and res[i] % 3 != 0 and res[i] % 5 != 0:
        #             res[i] = res[i] + 1
        #     return res[n-1]
        
# @lc code=end

