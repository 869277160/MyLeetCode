'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-21 23:50:37
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-21 23:56:03
FilePath: \Leetcode_Solver\2363.合并相似的物品.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2363 lang=python3
#
# [2363] 合并相似的物品
#

# @lc code=start
class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        
        import collections
        
        freq_1 = collections.Counter({item[0]:item[1] for item in items1})
        freq_2 = collections.Counter({item[0]:item[1] for item in items2})
        
        freq = freq_1 + freq_2
        
        res = [[key,freq[key]] for key in freq.keys()]
        
        return sorted(res,key=lambda x: x[0] )
        
        
# @lc code=end

