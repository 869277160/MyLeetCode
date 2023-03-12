'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-27 11:36:02
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-27 11:50:20
FilePath: \Leetcode_Solver\1323.6-和-9-组成的最大数字.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1323 lang=python3
#
# [1323] 6 和 9 组成的最大数字
#

# @lc code=start
class Solution:
    def maximum69Number (self, num: int) -> int:
        
        if num == 9999 or num == 999 or num == 99 or num == 9:
            return num
        
        string = str(num)
        
        for i in range(len(string)):
            if string[i] == '6':
                return int(string[:i]+'9'+string[i+1:])

        
        res = {
            6:9,
            9:9,
            66:96,
            69:99,
            96:99,
            99:99,
            666:966,
            669:969,
            696:996,
            699:999,
            966:996,
            969:999,
            996:999,
            999:999,
            6666:9666,
            6669:9669,
            6696:9696,
            6699:9699,
            6966:9966,
            6969:9969,
            6996:9996,
            6999:9999,
            9666:9966,
            9669:9969,
            9699:9999,
            9696:9996,
            9966:9996,
            9969:9999,
            9996:9999,
            9999:9999
            }
        
        return res[num]

        
# @lc code=end

