'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-27 18:14:09
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-27 18:34:45
FilePath: \Leetcode_Solver\2279.装满石头的背包的最大数量.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2279 lang=python3
#
# [2279] 装满石头的背包的最大数量
#

# @lc code=start
class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        
        current_cap = [capacity[i] - rocks[i] for i in range(len(capacity))]
        # import collections
        # freqs = collections.Counter(current_cap)
        # res = freqs[0] if 0 in freqs.keys() else 0
        # print(freqs)
        
        # sorted_keys = [key for key in freqs.keys() if key!=0]
        # sorted_keys.sort()
        
        
        current_cap.sort()
        sums = 0
        for i, r in enumerate(current_cap):
            sums += r
            if sums > additionalRocks: 
                return i
        return len(current_cap)


# @lc code=end

