'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-20 14:17:14
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-20 14:04:50
FilePath: \Leetcode_Solver\1002.查找共用字符.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1002 lang=python3
#
# [1002] 查找共用字符
#

# @lc code=start
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        
        import collections
        all_letters = [collections.Counter(i) for i in words]
        
        
        common_letter = all_letters[0]
        for all_letter in all_letters[1:]:
            common_letter = common_letter & all_letter
        
        res = []
        for key in common_letter.keys():
            for i in range(common_letter[key]):
                res.append(key)
        
        return res
        
# @lc code=end

