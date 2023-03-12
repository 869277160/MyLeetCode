'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-18 11:10:01
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-18 11:13:22
FilePath: \Leetcode_Solver\824.山羊拉丁文.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=824 lang=python3
#
# [824] 山羊拉丁文
#

# @lc code=start
class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        
        words = sentence.split(" ")
        
        res = ""
        for i in range(len(words)):
            word = words[i]
            temp = word
            
            # rule 1 
            if word[0] in "aeiouAEIOU":
                temp += "ma"
            
            # rule 2
            if word[0] not in "aeiouAEIOU":
                temp = temp[1:] + temp[0] + "ma"
            
            # rule 3 
            temp += "a" * (i+1)
            
            # concat outputs 
            res += temp + ' '
        
        # return and remove the last space 
        return res[:-1]
        
# @lc code=end

