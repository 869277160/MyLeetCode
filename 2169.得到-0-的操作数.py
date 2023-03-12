'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-07 17:35:57
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-07 17:51:25
FilePath: \Leetcode_Solver\2169.得到-0-的操作数.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2169 lang=python3
#
# [2169] 得到 0 的操作数
#

# @lc code=start
class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        
        
        if num1 == num2:
            return 1 if num1 != 0 else 0
        else :
            count = 0 
    
            while (num1 != 0 and num2 != 0):
                
                if  num1 >= num2:
                    num1 = num1 - num2
                else :
                    num2 = num2 - num1
                count += 1
                
                if num1 == num2:
                    return count+1
                elif num2 == 0 or num1 == 0 :
                    return count
                elif num1 == 1 or num2 ==1:
                    return count+num1 if num2 == 1 else count+num2
                
            return count
        
# @lc code=end

