'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-13 10:46:46
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-08-21 23:57:34
FilePath: \Leetcode_Solver\28.找出字符串中第一个匹配项的下标.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 找出字符串中第一个匹配项的下标
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # 1) use the python buildin function
        # return haystack.find(needle)
        
        # 2) search
        # len_txt = len(haystack)
        # len_pat = len(needle)
        # i,j = 0,0
        # while(i < len_txt and j < len_pat):
        #     if haystack[i] == needle[j]:
        #         i += 1 
        #         j += 1 
        #     else :
        #         i = i - j + 1
        #         j = 0
        # return i-j if (j == len_pat) else -1 
      
        
        # 3) KMP 
        len_txt = len(haystack)
        len_pat = len(needle)
        i,j = 0,0
        next_table = self.get_next_table(needle)
        while(i < len_txt and j < len_pat):
            if j == -1 or haystack[i] == needle[j]:
                i += 1 
                j += 1 
            else :
                j = next_table[j]
        return i-j if (j == len_pat) else -1 
        
        
    def get_next_table(self, pattern_str:str):
        
        pattern_len = len(pattern_str)
        next_table = [-1]*pattern_len
        # next_table[0] = -1
        
        k,j = -1, 0
        while(j < pattern_len-1):
            # k == -1 则为开头位置，因此一定会进入
            # 而后续判断条件则表示考虑到原有子串前后缀已经匹配的基础上，
            # 若现有子串前缀后的字符等于最后字符，则next更新，说明前后缀又匹配上了
            if (k == -1 or pattern_str[j] == pattern_str[k]):
                k+=1 
                j+=1
                # print(j)
                # print(next_table)
                # next_table[j] = k
                next_table[j] = k if pattern_str[j] != pattern_str[k] else next_table[k]
                
            else:
                k = next_table[k]
        
        return next_table
    
    def get_next_table_via_dp(self, patter_str:str):
        pattern_len = len(pattern_str)
        
# @lc code=end

if __name__ == "__main__":
    s = Solution()
    print(s.get_next_table("aaabbab"))