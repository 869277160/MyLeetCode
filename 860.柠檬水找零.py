'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-27 10:43:01
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-27 10:52:02
FilePath: \Leetcode_Solver\860.柠檬水找零.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=860 lang=python3
#
# [860] 柠檬水找零
#

# @lc code=start
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        if len(bills) == 0 :
            return True
        if bills[0] == 10 or bills[0] == 20:
            return False
        
        
        count5 = 0
        count10 = 0
        for i in bills:
            if i == 5 : 
                count5 +=1
            if i == 10 :
                if count5 < 0 :
                    return False
                else:
                    count5 -= 1
                    count10 += 1 
            if i == 20:
                if count10 >= 1 and count5 >= 1:
                    count5 -= 1
                    count10 -= 1
                elif count10 <= 0 and count5 >= 3:
                    count5 -=3
                else:
                    return False 
        
        return True 
# @lc code=end

