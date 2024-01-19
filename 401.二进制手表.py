'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-17 18:02:00
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-17 18:07:22
FilePath: \Leetcode_Solver\401.二进制手表.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=401 lang=python3
#
# [401] 二进制手表
#

# @lc code=start
class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        
        res_dict = []
        
        for i in range(0,12):
            for j in range(0,60):
                if bin(i).count("1") + bin(j).count("1") == turnedOn:
                    res_dict.append(str(i)+":"+str(j).zfill(2))
        
        return res_dict
        
# @lc code=end

