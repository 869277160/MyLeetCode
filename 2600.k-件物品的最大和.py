'''
Author: DingWang wangding19@mails.ucas.ac.cn
Date: 2024-01-29 20:53:01
LastEditors: DingWang wangding19@mails.ucas.ac.cn
LastEditTime: 2024-01-29 20:56:27
FilePath: \Leetcode_Solver\2600.k-件物品的最大和.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2600 lang=python3
#
# [2600] K 件物品的最大和
#

# @lc code=start
class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        if k <= numOnes:
            return k
        if k <= numOnes+numZeros:
            return numOnes
        else:
            return 2*numOnes - k +  numZeros
        
# @lc code=end

