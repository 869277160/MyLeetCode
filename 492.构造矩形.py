'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-16 09:35:51
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-16 09:40:34
FilePath: \Leetcode_Solver\492.构造矩形.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=492 lang=python3
#
# [492] 构造矩形
#

# @lc code=start
class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        import math
        
        all_LW = []
        for i in range(int(math.sqrt(area))+1,0,-1):
            if area % i == 0:
                return [max(area//i,i),min(area//i,i)]
                # return [area//i,i]
                # return all_LW[-1]












# @lc code=end

