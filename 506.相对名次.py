'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-20 21:23:07
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-20 21:24:51
FilePath: \Leetcode_Solver\506.相对名次.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=506 lang=python3
#
# [506] 相对名次
#

# @lc code=start
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        
        sorted_socre = sorted(score,reverse=True)
        
        outputs = ["Gold Medal","Silver Medal","Bronze Medal"] + [str(i) for i in range(4,len(score)+1)]
        
        for i in range(len(score)):
            score[i] = outputs[sorted_socre.index(score[i])]
        
        return score
        
        
        
        
        
        
        
# @lc code=end

