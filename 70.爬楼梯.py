'''
Author: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
Date: 2023-02-05 15:01:07
LastEditors: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
LastEditTime: 2023-02-05 15:02:44
FilePath: \Leetcode_Solver\70.爬楼梯.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''

def ClambStairs(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return ClambStairs(n-1) + ClambStairs(n-2)