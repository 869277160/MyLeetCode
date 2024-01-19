'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-17 16:41:42
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-17 17:12:10
FilePath: \Leetcode_Solver\873.最长的斐波那契子序列的长度.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=873 lang=python3
#
# [873] 最长的斐波那契子序列的长度
#

# @lc code=start
class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        
        res_dict = {}
        
        for i in range(len(arr)):
            if arr[i] not in res_dict.keys():
                res_dict[arr[i]] = []
            res_dict[arr[i]].append([0,2])
        
        # if arr[0] + arr[1] in arr:
        #     res_dict[arr[1]].append([0,2])
        
        
        for i in range(1,len(arr)):
            current_num = arr[i]
            if len(res_dict[current_num]) > 1:
                for j in range(1,len(res_dict[current_num])):
                    temp_total = current_num + res_dict[current_num][j][0]
                    if temp_total in arr:
                        temp_len = res_dict[current_num][j][1] + 1
                        res_dict[temp_total].append([current_num,temp_len])
            else :
                for j in range(0,i):
                    if arr[j] + arr[i] in arr:
                        res_dict[arr[i]+arr[j]].append([arr[i],3]) 
        print(res_dict)
        
        all_res = []
        for key in res_dict.keys():
            all_res.append(max([res_dict[key][i][1] for i in range(len(res_dict[key]))]))
        
        return max(all_res)
        
# @lc code=end

