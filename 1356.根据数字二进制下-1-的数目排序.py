'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-22 14:38:50
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-22 14:41:57
FilePath: \Leetcode_Solver\1356.根据数字二进制下-1-的数目排序.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1356 lang=python3
#
# [1356] 根据数字二进制下 1 的数目排序
#

# @lc code=start
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        order_dict = {i:bin(i).count("1") for i in arr}
        
        return sorted(arr,key= lambda x: (order_dict[x],x))
        
        
        
# @lc code=end

