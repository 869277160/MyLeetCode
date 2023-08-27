'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-17 17:30:09
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-17 17:31:50
FilePath: \Leetcode_Solver\14.最长公共前缀.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        res = ""
        for letter in strs[0]:
            res += letter
            for i in range(1,len(strs)):
                if res != strs[i][:len(res)]:
                    return res[:-1]
        return res
# @lc code=end

