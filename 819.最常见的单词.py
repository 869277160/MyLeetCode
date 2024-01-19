'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-17 10:50:36
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-18 11:06:34
FilePath: \Leetcode_Solver\819.最常见的单词.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=819 lang=python3
#
# [819] 最常见的单词
#

# @lc code=start
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        res_dict = {}
        
        paragraph = paragraph.replace(",", " ").replace(".", " ").replace("!", " ").replace("?", " ").replace(";", " ").replace("\'", " ")
        words = paragraph.lower().split(" ")
        
        for word in words :
            if word != "":
                if word in banned:
                    continue
                else :
                    if word in res_dict.keys():
                        res_dict[word] += 1
                    else:
                        res_dict[word] = 1
        
        for key, value in res_dict.items():
            if value == max(res_dict.values()):
                return key

        
# @lc code=end

