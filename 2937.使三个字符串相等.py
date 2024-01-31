'''
Author: DingWang wangding19@mails.ucas.ac.cn
Date: 2024-01-29 17:56:04
LastEditors: DingWang wangding19@mails.ucas.ac.cn
LastEditTime: 2024-01-29 18:15:28
FilePath: \Leetcode_Solver\2937.使三个字符串相等.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2937 lang=python3
#
# [2937] 使三个字符串相等
#

# @lc code=start
class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        # if len(s1) == len(s2) and len(s1) == len(s3):
        #     res = -1 
        #     
        #         for i in range(1, len(s1)):
        #             if s1[i] != s2[i] or s1[i] != s3[i] or s2[i] != s3[i]:
        #                 return (len(s1) - i)*3
        #         return 0
        #     else :
        #         return res
        if s1[0] == s2[0] and s3[0] == s2[0]:
            total_len = len(s1) + len(s2) + len(s3)
            min_len = min(len(s1) , len(s2) , len(s3))
            for i in range(1,min_len):
                if s1[i] != s2[i] or s1[i] != s3[i] or s2[i] != s3[i]:
                    return total_len - (i)*3
            return total_len - min_len*3
        else :
            return -1 
        
        # if len(s1) <= len(s2) and len(s1) <= len(s3):
        #     res = -1
        #     if s1[0] == s2[0] and s3[0] == s2[0]:
        #         for i in range(1, len(s1)):
        #             if s1[i] != s2[i] :
        #                 res += len(s1) - i + len(s2) - i
        #                 break
                    
        #         for i in range(1, len(s1)):
        #             if s1[i] != s2[i] :
        #                 res += len(s1) - i + len(s2) - i
        #                 break
        #             or s1[i] != s3[i] or s2[i] != s3[i]
                    
        #         return len(s3) + len(s2) - 2*len(s1)
        #     else :
        #             return res
        
        # if len(s2) <= len(s1) and len(s2) <= len(s3):
        #     for i in range(len(s2)):
        #         if s1[i] != s2[i] or s1[i] != s3[i] or s2[i] != s3[i]:
        #             return -1
        #     return len(s1) + len(s3) - 2*len(s2)
        
        # if len(s3) <= len(s1) and len(s3) <= len(s2):
            for i in range(len(s3)):
                if s1[i] != s2[i] or s1[i] != s3[i] or s2[i] != s3[i]:
                    return -1
            return len(s1) + len(s2) - 2*len(s3)
      

        # from collections import Counter
        # s1_count = Counter(s1) 
        # s2_count = Counter(s2) 
        # s3_count = Counter(s3) 
        
        
        
        
        
        
# @lc code=end

