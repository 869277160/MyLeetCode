'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-20 09:48:38
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-20 09:50:32
FilePath: \Leetcode_Solver\953.验证外星语词典.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=953 lang=python3
#
# [953] 验证外星语词典
#

# @lc code=start
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        # check length 
        length = [len(word) for word in words]
        for i in range(len(length)-1):
            if length[i] > length[i+1]:
                return False
        
        # check order
        for i in range(len(words)-1):
            for j in range(len(words[i])):
                if words[i][j] != words[i+1][j]:
                    if order.index(words[i][j]) > order.index(words[i+1][j]):
                        return False
                    else:
                        break
        
        return True
        
# @lc code=end

