'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-16 23:54:43
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-16 23:57:46
FilePath: \Leetcode_Solver\2194.excel-表中某个范围内的单元格.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2194 lang=python3
#
# [2194] Excel 表中某个范围内的单元格
#

# @lc code=start
class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        
        start_index= alphabet.index(s[0])
        end_index = alphabet.index(s[3])
        
        res= []
        for i in range(start_index,end_index+1):
            res += [alphabet[i]+str(j) for j in range(int(s[1]),int(s[4])+1)]
        return res 
# @lc code=end

