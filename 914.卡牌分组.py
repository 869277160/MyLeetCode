'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-20 20:17:18
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-20 20:23:01
FilePath: \Leetcode_Solver\914.卡牌分组.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=914 lang=python3
#
# [914] 卡牌分组
#

# @lc code=start
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        
        import collections
        
        freq = collections.Counter(deck)
        
        freq_list = list(freq.values())
        min_freq = min(freq_list)
        
        for i in range(2,min_freq+1):
            if all([freq% i == 0 for freq in freq_list]):
                return True
        # else:
        return False
        
        
        
        
# @lc code=end

