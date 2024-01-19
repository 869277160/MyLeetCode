'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-20 21:44:16
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-20 21:46:19
FilePath: \Leetcode_Solver\2558.从数量最多的堆取走礼物.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2558 lang=python3
#
# [2558] 从数量最多的堆取走礼物
#

# @lc code=start
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        
        if len(set(gifts)) == {1}:
            return len(gifts)
        
        import math
        for i in range(k):
            gifts[gifts.index(max(gifts))] = int(math.sqrt(max(gifts)))
        
        return sum(gifts)

# @lc code=end

