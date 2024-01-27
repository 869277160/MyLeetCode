'''
Author: DingWang wangding19@mails.ucas.ac.cn
Date: 2024-01-25 20:08:53
LastEditors: DingWang wangding19@mails.ucas.ac.cn
LastEditTime: 2024-01-25 21:26:12
FilePath: \Leetcode_Solver\89.格雷编码.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=89 lang=python3
#
# [89] 格雷编码
#
import math
# @lc code=start
class Solution:
    def __init__(self):
        self.res = []
        self.n = 0
    
    def grayCode(self, n: int) -> List[int]:
        if n == 1 :
            return [0,1]
        if n == 2 :
            return [0,1,3,2]
        else:
            temp_res = self.grayCode(n-1)
            for i in range(len(temp_res)-1,-1,-1):
                
                now_str = str(bin(temp_res[i]))[2:]
                if len(now_str) < n-1:
                    now_str = "0"*(n-len(now_str)-1) + now_str
                now_str = "1" + now_str
                temp_res.append(int(now_str,base=2))
            return temp_res
        
        
        
        
    #     self.n = n
    #     temp = ["0" for i in range(n)]
    #     idxs = [i for i in range(n)]
    #     self.traverse(temp, idxs, n)
        
    #     return self.res
    
    
    # def traverse(self, track, idxs, total):
    #     # print(self.res, track, idxs)
    #     if len(self.res) == 2**(self.n):
    #        return 
        
    #     temp = int("0b"+"".join(track),base=2)
    #     if temp not in self.res:
    #         self.res.append(temp)
    #     else:
    #         return 
    #     for i in range(len(idxs)-1,-1,-1):
    #         current_idx = idxs[i]
    #         if track[current_idx] == "0":
    #             track[current_idx] = "1"
    #             idxs = [i for i in range(total) if i != current_idx]
    #             self.traverse(track, idxs, total)
    #             track[current_idx] = "0"
    #         else:
    #             track[current_idx] = "0"
    #             idxs = [i for i in range(total) if i != current_idx]
    #             self.traverse(track, idxs, total)
    #             track[current_idx] = "1"
          
# @lc code=end

