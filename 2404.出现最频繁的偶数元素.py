'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-22 09:25:31
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-22 09:27:44
FilePath: \Leetcode_Solver\2404.出现最频繁的偶数元素.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2404 lang=python3
#
# [2404] 出现最频繁的偶数元素
#

# @lc code=start
class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        
        import collections
        
        freq = collections.Counter(nums)
        even_freq = {key:freq[key] for key in freq.keys() if key % 2 == 0}
        
        return max(even_freq,key=lambda x: (even_freq[x],-x)) if even_freq!= {} else -1
        
        
        
# @lc code=end

