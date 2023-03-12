'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-15 18:12:28
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-15 18:20:42
FilePath: \Leetcode_Solver\374.猜数字大小.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=374 lang=python3
#
# [374] 猜数字大小
#

# @lc code=start
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        
        if guess(n) == 0 :
            return n
        if guess(0) == 0 :
            return 0
        if guess(1) == 0 :
            return 0
        
        # 遍历标记
        res = -2
        current_max = n 
        guessing  = n // 2 
        current_min = 0
        
        # 中位数逼近
        while(res != 0):
            res = guess(guessing)
            
            if res == 1:
                current_min = guessing
            if res == -1:
                current_max = guessing
            if res == 0:
                return guessing
            
            # 下一个要猜测的节点
            guessing = (current_min + current_max) // 2
            
        

        
            
            
            
            
        
# @lc code=end

