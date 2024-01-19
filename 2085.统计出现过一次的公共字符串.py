'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-21 10:43:48
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-21 10:50:06
FilePath: \Leetcode_Solver\2085.统计出现过一次的公共字符串.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2085 lang=python3
#
# [2085] 统计出现过一次的公共字符串
#

# @lc code=start
class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        
        import collections
        
        freq_1 = collections.Counter(words1)
        freq_2 = collections.Counter(words2)
        
        count = 0
        for key in freq_1.keys():
            if key in freq_2.keys():
                if freq_1[key]==1 and freq_2[key]==1:
                    count+=1
        return count
        
        # return len([key for key in same.keys() if same[key]==1])
# @lc code=end

