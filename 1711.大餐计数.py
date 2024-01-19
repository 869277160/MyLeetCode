'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-04-14 17:08:53
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-04-14 17:54:01
FilePath: \Leetcode_Solver\1711.大餐计数.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1711 lang=python3
#
# [1711] 大餐计数
#

# @lc code=start
class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        
        import collections
        freq = collections.Counter(deliciousness)
        
        res = 0
        # # special_order_(2^(k-1) + 2^(k-1) and 2^k + 0 )
        # for i in range(0,20):
        #     if 2 ** i in freq.keys():
        #         res += freq[2 ** i] * (freq[2 ** i] - 1) // 2
        #         res += freq[2 ** i] * freq[0] if 0 in freq.keys() else 0
        #         res = res % (1e9+7)
        # # print(res)
        #         # if i != 0:
        #         #     freq.pop(2 ** i)
        # if 0 in freq.keys():
        #     freq.pop(0)
            
        
                
        # combine_orders

        # for i in range(0, 22):
        #     temp_key = list(freq.keys())
        #     # print(i)
        #     for j in temp_key:
        #         if j <= 2 ** i  and 2 ** i - j in freq.keys():
        #             if j == 2 ** (i-1):
        #                 res += freq[j] * (freq[j] - 1) // 2
        #                 res = res % (1e9+7)
        #             else :
        #                 res += (freq[j] * freq[2 ** i - j]) 
        #                 temp_key.remove(j)
        #                 temp_key.remove(2 ** i - j)
        #                 res = res % (1e9+7)
        #         # print(i,j,res)
        
        # return int(res)
        # return int(res_1) + int(res_2)
        
        # res = 0
        # for i in range(len(deliciousness)):
        #     for j in range(i,len(deliciousness)):
        #         if self.check(i+j) :
        #             res +=1
        #     deliciousness[i] = 2 ** deliciousness[i]
        
# @lc code=end

