'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-20 12:12:04
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-20 12:16:07
FilePath: \Leetcode_Solver\1897.重新分配字符使所有字符串都相等.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1897 lang=python3
#
# [1897] 重新分配字符使所有字符串都相等
#

# @lc code=start
class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        
        if len(words) == 1:
            return True
        
        
        import collections 
        all_words = "".join(words)
        counter = collections.Counter(all_words)
        
        # print(counter)
        # (1) 保证出现频率是字符串个数的整数倍
        for key in counter.keys():
            if counter[key] % len(words) != 0:
                return False
        
        return True 
        
        
# @lc code=end

