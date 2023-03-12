'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-17 09:25:22
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-09 09:19:54
FilePath: \Leetcode_Solver\2160.拆分数位后四位数字的最小和.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2160 lang=python3
#
# [2160] 拆分数位后四位数字的最小和
#

# @lc code=start
class Solution:
    def minimumSum(self, num: int) -> int:
        
        str_num = str(num)
        total_sum = [ ]

        total_sum.append(int(str_num[:1])+self.obtain_min(str_num[1:]))
        total_sum.append(self.obtain_min(str_num[:2])+self.obtain_min(str_num[2:]))
        total_sum.append(self.obtain_min(str_num[0]+str_num[3])+self.obtain_min(str_num[1:3]))
        total_sum.append(self.obtain_min(str_num[:3])+int(str_num[3:]))
        
        return min(total_sum)

    def obtain_min(self,num_str:str) -> int:
        res = 0
        if len(num_str) == 2:
            return min(int(num_str),int(num_str[1]+num_str[0]))
        else:
            res = "".join(sorted([i for i in num_str]))
            return int(res)
# 26+78
    
# @lc code=end

