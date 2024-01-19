'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-15 22:31:47
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-15 22:41:58
FilePath: \Leetcode_Solver\1837.k-进制表示下的各位数字总和.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1837 lang=python3
#
# [1837] K 进制表示下的各位数字总和
#

# @lc code=start
class Solution:
    def sumBase(self, n: int, k: int) -> int:
            
        res = 0
        while n:
            res += n % k
            n //= k
        return res
        
        
    #     if k == 10:
    #         return self.Sumallint(n)
    #     else:
    #         rest = n % k
    #         if rest < k:
    #             while(n > k):
    #                 n = n // k
    #                 rest += n % k
    #             return rest
    #         else:
    #             return self.Sumallint(n)
            
            
        
    # def Sumallint(self,n:int):
    #     s = str(n)
    #     res = 0
    #     for i in s :
    #         res += int(i)
    #     return res 

    # def Sumallstr(self,n:str):
    #     s = n
    #     res =0
    #     for i in s :
    #         res += int(i)
    #     return res 
    



# @lc code=end

