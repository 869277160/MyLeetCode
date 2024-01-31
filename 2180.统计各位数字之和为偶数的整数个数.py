'''
Author: DingWang wangding19@mails.ucas.ac.cn
Date: 2024-01-28 23:40:59
LastEditors: DingWang wangding19@mails.ucas.ac.cn
LastEditTime: 2024-01-29 00:02:40
FilePath: \Leetcode_Solver\2180.统计各位数字之和为偶数的整数个数.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2180 lang=python3
#
# [2180] 统计各位数字之和为偶数的整数个数
#

# @lc code=start
class Solution:
    def countEven(self, num: int) -> int:
        
        if num == 0 or num == 1:
            return 0
        elif num == 2:
            return 1
        elif num <= 8:
            return num // 2 
        elif num >8 and num <=10:
            return 4
        elif num > 10:
            self.res = 0
            for i in range(1, 10):
                self.traverse([i], i, num)
            return self.res 
        
    def traverse(self, track, now_input_num, num):
        # print(track, self.res)
        if now_input_num > num:
            return 
        if now_input_num <= num:
            if sum(track) % 2 == 0:
                
                self.res += 1
            
            for i in range(10):
                if now_input_num*10+i <= num:
                    self.traverse(track+[i], now_input_num*10+i, num)
            return 
# @lc code=end

