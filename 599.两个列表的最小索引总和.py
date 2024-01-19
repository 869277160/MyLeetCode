'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-20 21:00:02
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-20 21:01:12
FilePath: \Leetcode_Solver\599.两个列表的最小索引总和.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=599 lang=python3
#
# [599] 两个列表的最小索引总和
#

# @lc code=start
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:

        # list1_dict = {list1[i]:i for i in range(len(list1))}
        # list2_dict = {list2[i]:i for i in range(len(list2))}
        # list1_set = set(list1)
        # list2_set = set(list2)
        # common = list1_set & list2_set
        # common_dict = {common[i]:list1_dict[common[i]] + list2_dict[common[i]] for i in range(len(common))}
        # min_value = min(common_dict.values())
        # result = [key for key in common_dict.keys() if common_dict[key] == min_value]
        # return result

        list1_dict = {list1[i]:i for i in range(len(list1))}
        list2_dict = {list2[i]:i for i in range(len(list2))}
        list1_set = set(list1)
        list2_set = set(list2)
        common = list1_set & list2_set
        common = list(common)
        common_dict = {common[i]:list1_dict[common[i]] + list2_dict[common[i]] for i in range(len(common))}
        min_value = min(common_dict.values())
        result = [key for key in common_dict.keys() if common_dict[key] == min_value]
        return result








# @lc code=end

