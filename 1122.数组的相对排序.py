'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-20 23:01:14
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-20 23:04:07
FilePath: \Leetcode_Solver\1122.数组的相对排序.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1122 lang=python3
#
# [1122] 数组的相对排序
#

# @lc code=start
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        order_dict = {arr2[i]:i for i in range(len(arr2))}
        for i in arr1:
            if i not in order_dict.keys():
                order_dict[i] = len(arr2)

        return sorted(arr1,key= lambda x: (order_dict[x],x))



# @lc code=end

