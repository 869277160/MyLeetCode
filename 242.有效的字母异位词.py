'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-27 09:42:25
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-27 10:08:10
FilePath: \Leetcode_Solver\242.有效的字母异位词.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        s_dict = {}
        t_dict = {}
        
        # 循环构造哈希表，同时判断是否共享各个元素
        for i in s:
            if i not in t:
                return False
            else:
                if i not in s_dict:
                    s_dict[i] = 1
                s_dict[i] += 1 
        
        for j in t:
            if j not in s:
                return False
            else:
                if j not in t_dict:
                    t_dict[j] = 1
                t_dict[j] += 1
        
        
        if s_dict == t_dict:
            return True
        else :
            return False 
        
# @lc code=end

