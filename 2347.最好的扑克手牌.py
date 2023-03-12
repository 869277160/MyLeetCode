'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-05 13:08:46
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-05 16:26:20
FilePath: \Leetcode_Solverd:\Leetcode_Solver\2347.最好的扑克手牌.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2347 lang=python3
#
# [2347] 最好的扑克手牌
#

# @lc code=start
class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        
        if len(set(suits)) == 1:
            return "Flush"
        elif len(set(ranks)) == 2:
            return "Three of a Kind"
        elif len(set(ranks)) == 3:
            for i in ranks:
                if ranks.count(i) ==3:
                    return "Three of a Kind"
            return "Pair"
        elif len(set(ranks)) == 4:
            return "Pair"
        elif len(set(ranks))==5 :
            return "High Card"
        
    

# @lc code=end

