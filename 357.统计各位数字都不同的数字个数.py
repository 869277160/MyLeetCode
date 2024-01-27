'''
Author: DingWang wangding19@mails.ucas.ac.cn
Date: 2024-01-25 17:11:09
LastEditors: DingWang wangding19@mails.ucas.ac.cn
LastEditTime: 2024-01-25 17:30:51
FilePath: \Leetcode_Solver\357.统计各位数字都不同的数字个数.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=357 lang=python3
#
# [357] 统计各位数字都不同的数字个数
#
from collections import Counter 
# @lc code=start
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 10
        if n == 2:
            return 91
        
        self.res = 0
        all_num = [i for i in range(0,10)]
        for i in range(1,len(all_num)):
            self.traverse(all_num[:i]+all_num[i+1:], n, [all_num[i]])
        
        return self.res + 1
    
    def traverse(self, all_num, n, track):
        # print(all_num, track)
        if self.is_unique(track):
            self.res += 1
        if len(track) == n:
            return
        
        for i in range(0,len(all_num)):
            if all_num[i] not in track:
                self.traverse(all_num[:i]+all_num[i+1:], n, track+[all_num[i]])
    
    def is_unique(self, nums):
        count = Counter(nums)
        for i in count:
            if count[i] > 1 :
                return False
        return True 
# @lc code=end

