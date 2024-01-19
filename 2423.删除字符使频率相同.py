'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-22 09:29:52
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-22 09:50:53
FilePath: \Leetcode_Solver\2423.删除字符使频率相同.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2423 lang=python3
#
# [2423] 删除字符使频率相同
#

# @lc code=start
import collections


class Solution:
    def equalFrequency(self, word: str) -> bool:
        

        
        def is_same_freq(s):
            freq = collections.Counter(s)
            
            for key in freq.keys():
                if freq[key] != freq[s[0]]:
                    return False
            
            return True 
        
        # 对最低的频率和最高频率进行删除
        freq = collections.Counter(word)
        words = [i for i in word]
        words = sorted(words, key=lambda x: freq[x])
        
        return is_same_freq(words[1:]) or is_same_freq(words[:-1])
        
# @lc code=end

