'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-24 16:48:31
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-24 16:49:29
FilePath: \Leetcode_Solver\386.字典序排数.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=386 lang=python3
#
# [386] 字典序排数
#

# @lc code=start
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        
        res = [i for i in range(1,n+1)]
        res.sort(key=lambda x: str(x))
        
        return res 
        
        
        
        
# @lc code=end

