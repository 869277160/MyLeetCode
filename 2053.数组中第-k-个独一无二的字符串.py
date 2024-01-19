'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-21 10:21:10
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-21 10:28:25
FilePath: \Leetcode_Solver\2053.数组中第-k-个独一无二的字符串.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2053 lang=python3
#
# [2053] 数组中第 K 个独一无二的字符串
#

# @lc code=start
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        import collections
        arr_index = {arr[i]:i for i in range(len(arr))}
        freq = collections.Counter(arr)
        arr = sorted(arr,key = lambda x: (freq[x],arr_index[x]))
        
        res = arr[k-1]
        if freq[res] == 1:
            return res
        else:
            return ""
        
        
# @lc code=end

