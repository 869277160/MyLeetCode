'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-05 11:20:10
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-05 11:45:49
FilePath: \Leetcode_Solverd:\Leetcode_Solver\728.自除数.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=728 lang=python3
#
# [728] 自除数
#

# @lc code=start
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        

        res = []
        for i in range(left,right+1):
            if self.check_self_dividing(i):
                res.append(i)
        
        return res 

    def check_self_dividing(self, num):
        if num < 10:
            return True
        # elif num % 11 == 0 and num % 10 != 0:
        #     return True
        else:
            num_str = str(num)
            for i in range(len(num_str)):
                if num_str[i] == '0' :
                    return False 
                # if num_str[i] == '1':
                #     pass 
                if num % int(num_str[i]) != 0:
                    return False
            return True
        
        
        
        
        
# @lc code=end

