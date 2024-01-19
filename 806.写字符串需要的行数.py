'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-16 12:30:10
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-16 12:34:20
FilePath: \Leetcode_Solver\806.写字符串需要的行数.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=806 lang=python3
#
# [806] 写字符串需要的行数
#

# @lc code=start
class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        
        lines= 0
        current_row = 0 
        for i in range(len(s)):
            
            if current_row == 100:
                lines += 1
                current_row = 0
            
            current_row += widths[ord(s[i])-97]
            
            if current_row > 100 :
                lines += 1 
                current_row = widths[ord(s[i])-97]

            # print(lines, current_row)
        
        return [lines+1,current_row]
        
        
        
        
# @lc code=end

