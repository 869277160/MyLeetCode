'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-16 22:17:07
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-16 22:28:11
FilePath: \Leetcode_Solver\2582.递枕头.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2582 lang=python3
#
# [2582] 递枕头
#

# @lc code=start
class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        
        res = [1]
        while(len(res) < time+1):
            res += [i for i in range(2,n+1)]
            res += [i for i in range(n-1,0,-1)]
      
        return res[time]    
        
        # if ((time // (n -1)) +1) % 2 == 0:
            
            
        #     return n- (time% (n -1))
        # else:
        #     res_list = []
        #     res = time % (n -1) +1 
        #     if res == n:
        #         return 1
        #     return  + 1
            
        
        
        
        
# @lc code=end

