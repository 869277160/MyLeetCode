'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-16 20:40:22
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-16 20:43:32
FilePath: \Leetcode_Solver\258.各位相加.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=258 lang=python3
#
# [258] 各位相加
#

# @lc code=start
class Solution:
    def addDigits(self, num: int) -> int:
        
        if num < 10 :
            return num
        else:
            res = sum([int(i) for i in str(num)])
            
            # 手动循环加，先加最后的，在整除一下
            # res = 0
            # while num:
            #     res += num % 10
            #     num //= 10

            if res < 10:
                return res
            else:
                return self.addDigits(res)
        
        
# @lc code=end

