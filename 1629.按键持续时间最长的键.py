'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-16 22:45:53
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-16 22:53:53
FilePath: \Leetcode_Solver\1629.按键持续时间最长的键.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1629 lang=python3
#
# [1629] 按键持续时间最长的键
#

# @lc code=start
class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        
        each_time = [releaseTimes[0]]+[releaseTimes[i+1]-releaseTimes[i] for i in range(len(releaseTimes)-1)]
        
        dict_time = {}
        for i in range(0,len(keysPressed)):
            letter = keysPressed[i]
            if letter not in dict_time.keys():
                dict_time[letter] = 0
            if each_time[i] > dict_time[letter]:
                dict_time[letter] = each_time[i]
        
        max_time = max(dict_time.values())
        
        all_letter = [i for i in dict_time.keys() if dict_time[i] == max_time]
        # print(all_letter)
        
        return max(all_letter)

# @lc code=end

