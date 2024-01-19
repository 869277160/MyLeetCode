'''
Author: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
Date: 2023-02-07 09:38:05
LastEditors: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
LastEditTime: 2023-02-07 10:04:22
FilePath: \Leetcode_Solver\12.整数转罗马数字.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=12 lang=python3
#
# [12] 整数转罗马数字
#

# @lc code=start
class Solution:
    # 类似进制转化，但是更加简单，只需要按顺序mod值即可
    def intToRoman(self, num: int) -> str:
        
        mod_elems = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
    
        elems = {1:"I",5:"V",10:"X",50:"L",100:"C",500:"D",1000:"M",4:"IV",9:"IX",40:"XL",90:"XC",400:"CD",900:"CM",}
        res = ""
        input = num
        
        for mod_elem in mod_elems:
            left = input % mod_elem
            if left < input:
                for j in range((input-left) // mod_elem):
                    res += elems[mod_elem]
            input = left

        return res
# @lc code=end

