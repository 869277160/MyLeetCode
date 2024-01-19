'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-05 12:01:33
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-05 12:23:24
FilePath: \Leetcode_Solverd:\Leetcode_Solver\1640.能否连接形成数组.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1640 lang=python3
#
# [1640] 能否连接形成数组
#

# @lc code=start
class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        Headers = [piece[0] for piece in pieces]
        i = 0 
        while(i < len(arr)):
            if arr[i] in Headers:
                piece = pieces[Headers.index(arr[i])]
                if arr[i:i+len(piece)] == piece:
                    i+=len(piece)
                else :
                    return False 
            else:
                return False

        return True

    # def Matchpieces(self,arr, i , piece):
    #     # res = -1 
    #     for j in range(0,len(piece)):
    #         if piece[j] != arr[i+j]:
    #             return False, -1
    #         else :
    #             pass
    #         return True, len(piece) 
            
    #     return False, -1

