'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-20 14:56:54
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-20 14:57:19
FilePath: \Leetcode_Solver\1108.ip-地址无效化.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1108 lang=python3
#
# [1108] IP 地址无效化
#

# @lc code=start
class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".","[.]")
# @lc code=end

