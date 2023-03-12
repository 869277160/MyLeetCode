'''
Author: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
Date: 2023-02-09 09:26:49
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-13 17:02:32
FilePath: \Leetcode_Solver\17.电话号码的字母组合.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num_dict = {
            2:["a","b","c"],
            3:["d","e","f"],
            4:["g","h","i"],
            5:["j","k","l"],
            6:["m","n","o"],
            7:["p","q","r","s"],
            8:["t","u","v"],
            9:["w","x","y","z"],
        }
        
        if len(digits) == 0:
            return []
        elif len(digits) == 1:
            return num_dict[int(digits)]
        elif len(digits) == 2:
            return self.CombineN([num_dict[int(digits[0])],num_dict[int(digits[1])]])
        elif len(digits) == 3:
            return self.CombineN([num_dict[int(digits[0])],num_dict[int(digits[1])],num_dict[int(digits[2])]])
        elif len(digits) == 4:
            return self.CombineN([num_dict[int(digits[0])],num_dict[int(digits[1])],num_dict[int(digits[2])],num_dict[int(digits[3])]])

                
                
    def CombineN(self,strlists):
        if len(strlists) == 2 :
            return [i+j for i in strlists[0] for j in strlists[1]]
        if len(strlists) == 3 :
                return [i+j+k for i in strlists[0] for j in strlists[1] for k in strlists[2]]
        if len(strlists) == 4 :
                return [i+j+k+l for i in strlists[0] for j in strlists[1] for k in strlists[2] for l in strlists[3]]

# @lc code=end

