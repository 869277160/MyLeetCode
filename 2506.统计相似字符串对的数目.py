'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-20 19:29:23
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-20 19:34:01
FilePath: \Leetcode_Solver\2506.统计相似字符串对的数目.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2506 lang=python3
#
# [2506] 统计相似字符串对的数目
#

# @lc code=start
class Solution:
    def similarPairs(self, words: List[str]) -> int:
        
        word_set = [set(word) for word in words]
        
        count = 0
        for i in range(0,len(words)):
            for j in range(i+1,len(words)):
                if (word_set[i] == word_set[j]):
                    count +=1 
        
        # print(count)
        
        return count
        
# @lc code=end

