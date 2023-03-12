'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-16 22:34:56
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-16 22:47:23
FilePath: \Leetcode_Solver\717.1-比特与-2-比特字符.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=717 lang=python3
#
# [717] 1 比特与 2 比特字符
#

# @lc code=start
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        if len(bits) == 0:
            return 0
        if len(bits) == 1:
            if bits == [0]:
                return True
            else :
                return False 
        if len(bits) == 2:
            if bits == [1,0] or bits == [1,1] or bits == [0,1]:
                return False
            if bits == [0,0]:
                return True
        if len(bits) > 2:
            if bits[:2] == [1,0] or bits[:2] == [1,1] or bits[:2] == [0,0]:
                return self.isOneBitCharacter(bits[2:])
            if bits[:2] == [0,1]:
                return self.isOneBitCharacter(bits[1:])
            
# @lc code=end

