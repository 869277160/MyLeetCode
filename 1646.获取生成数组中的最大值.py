'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-27 22:03:19
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-27 22:08:16
FilePath: \Leetcode_Solver\1646.获取生成数组中的最大值.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1646 lang=python3
#
# [1646] 获取生成数组中的最大值
#

# @lc code=start
class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        
        res = [0,1,1,2,1,3,2,3]
        if n <= 7 :
            return max(res[:n+1])
        else:
            for i in range(8,n+1):
                if i % 2 == 0:
                    res.append(res[i//2])
                else :
                    res.append(res[i//2] + res[i//2 + 1])
            return max(res[:n+1])

# @lc code=end

