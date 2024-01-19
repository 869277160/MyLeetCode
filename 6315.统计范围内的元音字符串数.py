'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-16 22:30:17
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-16 22:32:03
FilePath: \Leetcode_Solver\6315.统计范围内的元音字符串数.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=6315 lang=python3
#
# [6315] 统计范围内的元音字符串数
#

# @lc code=start
class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        
        count = 0
        checker = "aeiou"
        for i in range(left,right+1):
            if words[i][0] in checker and words[i][-1] in checker:
                count += 1

        return count
# @lc code=end

