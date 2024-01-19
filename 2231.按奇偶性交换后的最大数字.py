'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-23 09:31:56
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-23 09:37:13
FilePath: \Leetcode_Solver\2231.按奇偶性交换后的最大数字.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2231 lang=python3
#
# [2231] 按奇偶性交换后的最大数字
#

# @lc code=start
class Solution:
    def largestInteger(self, num: int) -> int:
        
        # 1. 先将数字转换为字符串, 然后将奇数和偶数分别存储到两个列表中
        odd =[i for i in str(num) if int(i) % 2 == 1]
        odd.sort(reverse=True)
        even = [i for i in str(num) if int(i)% 2!= 1]
        even.sort(reverse=True)
        
        # 2. 从左到右遍历字符串,
        # 如果是奇数, 则从奇数列表中取出最大的数字, 
        # 如果是偶数, 则从偶数列表中取出最大的数字
        res = ""
        odd_pos = 0
        even_pos = 0
        for i in range(len(str(num))):
            if int(str(num)[i]) % 2 == 1:
                res += str(odd[odd_pos])
                odd_pos += 1
            else:
                res += str(even[even_pos])
                even_pos += 1
        
        # 3. 返回结果
        return int(res if res[0] != "0" else "0")

        
        
        
        
# @lc code=end

