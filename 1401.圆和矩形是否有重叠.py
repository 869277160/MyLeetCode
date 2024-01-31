'''
Author: DingWang wangding19@mails.ucas.ac.cn
Date: 2024-01-30 16:05:31
LastEditors: DingWang wangding19@mails.ucas.ac.cn
LastEditTime: 2024-01-30 16:23:51
FilePath: \Leetcode_Solver\1401.圆和矩形是否有重叠.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1401 lang=python3
#
# [1401] 圆和矩形是否有重叠
#

# @lc code=start
class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        # def lengths(x, y):
        #     return x**2 + y**2
        
        # len_1 = lengths(abs(x1-xCenter), abs(y1-yCenter))
        # len_2 = lengths(abs(x1-xCenter), abs(y2-yCenter))
        # len_3 = lengths(abs(x2-xCenter), abs(y1-yCenter))
        # len_4 = lengths(abs(x2-xCenter), abs(y2-yCenter))
        
        # print(len_1,len_2,len_3,len_4)
        # min_len = min(len_1,len_2,len_3,len_4)
        # if min_len <= radius:
        #     return True 
        # else:
        #     if len_1 == len_2 and len_1 == min_len:
        #         if min_len == radius**2 + (abs(y2-y1)//2) ** 2:
        #             return True
        #         else:
        #             return False
        #     if len_1 == len_3 and len_1 == min_len:
        #         if min_len == radius**2 + (abs(x2-x1)//2) ** 2:
        #             return True
        #         else:
        #             return False
        #     if len_2 == len_4 and len_1 == min_len:
        #         if min_len == radius**2 + (abs(x2-x1)//2) ** 2:
        #             return True
        #         else:
        #             return False
        #     if len_3 == len_4 and len_1 == min_len:
        #         if min_len == radius**2 + (abs(y2-y1)//2) ** 2:
        #             return True
        #         else:
        #             return False

        #     return False
        
        
        def f(i: int, j: int, k: int) -> int:
            if i <= k <= j:
                return 0
            return i - k if k < i else k - j

        a = f(x1, x2, xCenter)
        b = f(y1, y2, yCenter)
        return a * a + b * b <= radius * radius

        
        
# @lc code=end

