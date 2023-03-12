'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-21 09:52:47
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-21 10:00:35
FilePath: \Leetcode_Solver\1309.解码字母到整数映射.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1309 lang=python3
#
# [1309] 解码字母到整数映射
#

# @lc code=start
class Solution:
    def freqAlphabets(self, s: str) -> str:
        
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        
        res = ""
        i = 0 
        while i < len(s):
            # 当前是否为# 
            if i != "#":
                # 如果后续还有#的空间
                if i < len(s)-2 :
                    # 如果后续为#,联合解析
                    if s[i+2] == "#":
                        res += alphabet[int(s[i:i+2])-1]
                        i+=3
                    # 否则直接解析
                    else:
                        res += alphabet[int(s[i])-1]
                        i+=1
                # 没有空间,直接解析即可
                else:
                    res += alphabet[int(s[i])-1]
                    i+=1
            # 当前为#
            else :
                i +=1 
            
        
        return  res 
        
        
# @lc code=end

