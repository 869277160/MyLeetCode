'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-16 23:40:57
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-16 10:44:28
FilePath: \Leetcode_Solver\925.长按键入.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=925 lang=python3
#
# [925] 长按键入
#

# @lc code=start

# 用正则表达式进行解决？
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        # 用双指针进行解决？
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        if len(typed) < len(name): return False
        elif len(typed) == len(name) and typed != name: return False

        i, j = 0, 0
        while i<len(name):
            if i+1<len(name) and name[i+1]==name[i]:
                if name[i] == typed[j]:
                    i += 1
                    j += 1
                else:
                    return False
            else:
                if j>=len(typed):
                    return False
                if name[i] != typed[j]:
                    return False
                while j<len(typed) and typed[j] == name[i]:
                    j += 1
                i += 1
        if j<len(typed) and typed[j]!=name[-1]:
            return False
        return True


        
        
        
        
        
# @lc code=end

