'''
Author: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
Date: 2023-02-06 10:30:44
LastEditors: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
LastEditTime: 2023-02-06 10:34:03
FilePath: \Leetcode_Solver\397.整数替换.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=397 lang=python3
#
# [397] 整数替换
#

# @lc code=start
class Solution:
    def integerReplacement(self, n: int) -> int:
        return  self.Looping(n,0)

    def Looping(self,n,count):
        if n == 1: return count 
        elif n == 2: return count + 1
        else:
            if n % 2 == 0 :
                return self.Looping(n//2,count+1)
            else :
                return min(self.Looping(n+1,count+1),self.Looping(n-1,count+1))
          
# @lc code=end

