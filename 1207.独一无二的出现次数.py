'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-21 10:15:15
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-01 09:43:39
FilePath: \Leetcode_Solver\1207.独一无二的出现次数.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1207 lang=python3
#
# [1207] 独一无二的出现次数
#

# @lc code=start
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        num_dict = {}
        
        for i in arr:
            if i not in num_dict.keys():
                num_dict[i] = 0
            num_dict[i] +=1 
        
        if len(num_dict.values()) == len(set(num_dict.values())):
            return True
        else:
            return False 
        
# @lc code=end

