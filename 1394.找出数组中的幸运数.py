'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-21 11:03:43
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-21 11:04:49
FilePath: \Leetcode_Solver\1394.找出数组中的幸运数.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1394 lang=python3
#
# [1394] 找出数组中的幸运数
#

# @lc code=start
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        
        counter = [0] * (max(arr)+1)
        
        for i in arr:
            counter[i] += 1 
        
        for i in range(len(counter)-1,0,-1):
            if counter[i] == i:
                return i
            
        return -1 
        
        
# @lc code=end

