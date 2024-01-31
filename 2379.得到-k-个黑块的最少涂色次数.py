'''
Author: DingWang wangding19@mails.ucas.ac.cn
Date: 2024-01-29 22:29:39
LastEditors: DingWang wangding19@mails.ucas.ac.cn
LastEditTime: 2024-01-29 22:35:20
FilePath: \Leetcode_Solver\2379.得到-k-个黑块的最少涂色次数.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2379 lang=python3
#
# [2379] 得到 K 个黑块的最少涂色次数
#

# @lc code=start
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        # if len(blocks) == k:
        #     return blocks.count("W")
        res = [len(blocks) for _ in range(len(blocks)-k+1)]
        for i in range(len(blocks)-k+1):
            print(blocks[i:i+k])
            res[i] = blocks[i:i+k].count("W")
        # print(res)
        return min(res)
            
# @lc code=end

