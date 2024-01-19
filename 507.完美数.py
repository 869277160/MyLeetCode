'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-13 11:13:28
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-13 11:26:28
FilePath: \Leetcode_Solver\507.完美数.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=507 lang=python3
#
# [507] 完美数
#

# @lc code=start
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        
        import math 
        
        total = 1
        for i in range(2,int(math.sqrt(num))+1):
            if num % i == 0:
                total += i
                total += num//i
            
        if(int(math.sqrt(num)) *int(math.sqrt(num)) == num):
            total += math.sqrt(num);
            
        return total == num
        
    
    # def checkPerfectNumber(self, num):
    #     return True if num in [6, 28, 496, 8128, 33550336] else False
# @lc code=end

