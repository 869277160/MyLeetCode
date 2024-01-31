'''
Author: DingWang wangding19@mails.ucas.ac.cn
Date: 2024-01-29 15:14:41
LastEditors: DingWang wangding19@mails.ucas.ac.cn
LastEditTime: 2024-01-29 15:17:28
FilePath: \Leetcode_Solver\2287.重排字符形成目标字符串.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2287 lang=python3
#
# [2287] 重排字符形成目标字符串
#

# @lc code=start
class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        from collections import Counter
        
        s_count = Counter(s)
        t_count = Counter(target)
        
        res = len(s)
        for c in t_count:
            if c not in s_count:
                return 0
            else:
                if s_count[c] < t_count[c]:
                    return 0
                else:
                    res = min(res, s_count[c] // t_count[c])
        return res 
# @lc code=end

