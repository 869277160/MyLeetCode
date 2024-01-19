'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-21 09:27:40
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-21 09:28:59
FilePath: \Leetcode_Solver\1720.解码异或后的数组.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1720 lang=python3
#
# [1720] 解码异或后的数组
#

# @lc code=start
class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        res = [first]
        for i in range(len(encoded)):
            res.append(res[i]^encoded[i])
        return res  


# @lc code=end


