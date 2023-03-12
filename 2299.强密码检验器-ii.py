'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-21 10:57:27
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-21 11:01:38
FilePath: \Leetcode_Solver\2299.强密码检验器-ii.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2299 lang=python3
#
# [2299] 强密码检验器 II
#

# @lc code=start
class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        
        if len(password) < 8:
            return False 
        if self.checklow(password) == False:
            return False
        if self.checkhigh(password) == False:
            return False
        if self.checknum(password) == False:
            return False
        if self.checkrepeat(password) == False:
            return False
        if self.checkspecial(password) == False:
            return False 
        
        return True 
    
    def checklow(self, password):
        for i in password:
            if i.islower():
                return True 
        return False
    
    def checkhigh(self, password):
        for i in password:
            if i.isupper():
                return True 
        return False
    
    def checknum(self, password):
        for i in password:
            if i.isdigit():
                return True 
        return False
    
    def checkrepeat(self,password):
        for i in range(len(password)-1):
            if password[i] == password[i+1]:
                return False
        return True
    
    def checkspecial(self,password):
        specical = "!@#$%^&*()-+"
        for i in password:
            if i in specical:
                return True 
        return False 
    
# @lc code=end

