'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-18 15:56:05
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-18 16:04:30
FilePath: \Leetcode_Solver\1652.拆炸弹.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1652 lang=python3
#
# [1652] 拆炸弹
#

# @lc code=start
class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:

        if k == 0:
            return [0] * len(code)
        if k > 0:
            code = code + code
            res = [0] * (len(code)//2)
            for i in range(len(code)//2):
                res[i] = sum(code[i+1:i+k+1])
            return res
        if k <0:
            code = code + code
            res = [0] * (len(code)//2)
            # 两个部分拼接
            for i in range(len(code)//2,len(code)):
                res[i-(len(code)//2)] = sum(code[i+k:i])
            return res
            
# @lc code=end

