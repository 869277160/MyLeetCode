'''
Author: DingWang wangding19@mails.ucas.ac.cn
Date: 2024-01-28 23:00:27
LastEditors: DingWang wangding19@mails.ucas.ac.cn
LastEditTime: 2024-01-28 23:08:13
FilePath: \Leetcode_Solver\1317.将整数转换为两个无零整数的和.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1317 lang=python3
#
# [1317] 将整数转换为两个无零整数的和
#

# @lc code=start
class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        if n < 10:
            return [1, n-1]
        else:
            temp =  [i for i in range(1,10)] +\
                    [i for i in range(11,20)] + \
                    [i for i in range(111,119)]
            for i in range(len(temp)):
                if not self.is_None_Zero(n-temp[i]):
                    return [temp[i],n-temp[i]]
    
    def is_None_Zero(self, n):
        if n % 10 == 0:
            return True 
        
        for i in range(len(str(n))):
            if str(n)[i] == "0":
                return True

        return False 
# @lc code=end

