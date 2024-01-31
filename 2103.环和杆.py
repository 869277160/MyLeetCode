'''
Author: DingWang wangding19@mails.ucas.ac.cn
Date: 2024-01-28 23:33:53
LastEditors: DingWang wangding19@mails.ucas.ac.cn
LastEditTime: 2024-01-28 23:36:29
FilePath: \Leetcode_Solver\2103.环和杆.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2103 lang=python3
#
# [2103] 环和杆
#

# @lc code=start
class Solution:
    def countPoints(self, rings: str) -> int:
        res = ["" for i in range(11)]
        for i in range(0, len(rings), 2):
            if rings[i] not in res[int(rings[i+1])]:
                res[int(rings[i+1])] += rings[i]

        
        print(res)
        return res.count("RGB") + res.count("RBG") + \
            res.count("GRB") + res.count("GBR") + \
            res.count("BRG") + res.count("BGR") 
# @lc code=end

