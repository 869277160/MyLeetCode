'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-20 23:06:12
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-20 23:13:14
FilePath: \Leetcode_Solver\1221.分割平衡字符串.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1221 lang=python3
#
# [1221] 分割平衡字符串
#

# @lc code=start
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        
        count = 0
        while(s != ""):
            s = self.split_str(s)
            count +=1
            # print(s)
        
        return count
            
                
    def split_str(self, s):
        import collections
        
        for i in range(2,len(s),2):
            freq = collections.Counter(s[:i])
            if freq["L"] == freq["R"]:
                return s[i:]
            
        return ""        
        
# @lc code=end

