'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-05 11:55:32
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-05 12:00:34
FilePath: \Leetcode_Solverd:\Leetcode_Solver\2073.买票需要的时间.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2073 lang=python3
#
# [2073] 买票需要的时间
#

# @lc code=start
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        
        if tickets[k] == min(tickets):
            return tickets[k]*len(tickets)-(len(tickets)-k-1)
        else :
            count = 0
            while(tickets[k]!=0):
                for i in range(len(tickets)):
                    if tickets[i] != 0:
                        tickets[i] -= 1
                        count += 1
                    if tickets[k] == 0:
                        return count
                
            return count

        
# @lc code=end

