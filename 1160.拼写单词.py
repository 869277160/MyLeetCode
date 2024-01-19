'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-16 22:37:05
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-16 22:44:08
FilePath: \Leetcode_Solver\1160.拼写单词.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1160 lang=python3
#
# [1160] 拼写单词
#

# @lc code=start
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        
        learned_dict = {}
        for char in chars:
            if char not in learned_dict.keys():
                learned_dict[char] = 0
            learned_dict[char] += 1
        
        res = 0
        for word in words:
            temp = learned_dict.copy()
            res += self.check(word, temp)
            # print(learned_dict)
            
        return res
    
    def check(self, word, learned_dict):

        # word_dict = {}
        for i in word:
            if i not in learned_dict.keys():
                return 0
            else:
                learned_dict[i] -= 1 
                if learned_dict[i] < 0:
                    return 0
                
        return len(word)
    
# @lc code=end

