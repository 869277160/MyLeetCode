'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-20 11:28:20
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-20 11:30:14
FilePath: \Leetcode_Solver\2566.替换一个数字后的最大差值.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2566 lang=python3
#
# [2566] 替换一个数字后的最大差值
#

# @lc code=start
class Solution:
    def minMaxDifference(self, num: int) -> int:
        
        # str_num = str(num)
        # m, M = 0xFFFFFFFF, 0
        # for i in range(10):
        #     for j in range(10):
        #         new = int(str_num.replace(str(i), str(j)))
        #         m = min(m, new)
        #         M = max(M, new)
        # return M - m

        
        str_num = str(num)
        minimum = int(str_num.replace(str_num[0], '0'))
        n = len(str_num)
        for i in range(n):
            if str_num[i] != '9':
                return int(str_num.replace(str_num[i], '9')) - minimum
        return num # 全部数字均为 9 时返回本身即可

# @lc code=end

