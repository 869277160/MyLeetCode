'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-21 10:16:14
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-21 10:20:56
FilePath: \Leetcode_Solver\1945.字符串转化后的各位数字之和.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1945 lang=python3
#
# [1945] 字符串转化后的各位数字之和
#

# @lc code=start
class Solution:
    def getLucky(self, s: str, k: int) -> int:
        
        num = self.str2num(s)
        
        num = self.strnum2sum(num)
        for _ in range(k-1):
            num = self.num2sum(num)

        return num        
    
    def str2num(self,s):
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        
        res = ""
        for i in s:
            res+= str(alphabet.index(i)+1)
        
        return res 

    def num2sum(self,num):
        res =0
        while(num):
            res += num%10
            num = num//10
        return res
        
    def strnum2sum(self,num):
        res =0
        for i in (num):
            res += int(i)
        return res
        
# @lc code=end

