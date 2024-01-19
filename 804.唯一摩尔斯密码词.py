'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-17 10:44:45
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-17 10:49:44
FilePath: \Leetcode_Solver\804.唯一摩尔斯密码词.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=804 lang=python3
#
# [804] 唯一摩尔斯密码词
#

# @lc code=start
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        
        letter_dict = {}
        letter_moss = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        letter = "abcdefghijklmnopqrstuvwxyz"

        for i in range(26):
            letter_dict[letter[i]]=letter_moss[i]
        
        word_moss_dict = {}
        
        for word in words:
            word_moss = ""
            for letter in word:
                word_moss += letter_dict[letter]
            if word_moss in word_moss_dict.keys():
                word_moss_dict[word_moss] += 1
            else :
                word_moss_dict[word_moss] = 1
        
        return len(word_moss_dict.keys())
        
# @lc code=end

