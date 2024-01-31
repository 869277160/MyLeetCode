'''
Author: DingWang wangding19@mails.ucas.ac.cn
Date: 2024-01-29 18:25:28
LastEditors: DingWang wangding19@mails.ucas.ac.cn
LastEditTime: 2024-01-29 18:25:58
FilePath: \Leetcode_Solver\2929.给小朋友们分糖果-ii.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2929 lang=python3
#
# [2929] 给小朋友们分糖果 II
#

# @lc code=start
class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        # res =0 
        # for i in range(0, limit+1):
        #     for j in range(0, limit+1):
        #         # print(i,j,n - i - j)
        #         if n - i - j <= limit and n - i - j >= 0:
        #             res +=1
        # return res
        
        def c2(n: int) -> int:
            return n * (n - 1) // 2 if n > 1 else 0

        return c2(n + 2) - 3 * c2(n - limit + 1) + 3 * c2(n - 2 * limit) - c2(n - 3 * limit - 1)


# @lc code=end

