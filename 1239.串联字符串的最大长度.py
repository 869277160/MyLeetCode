'''
Author: DingWang wangding19@mails.ucas.ac.cn
Date: 2024-01-30 15:27:20
LastEditors: DingWang wangding19@mails.ucas.ac.cn
LastEditTime: 2024-01-30 15:39:58
FilePath: \Leetcode_Solver\1239.串联字符串的最大长度.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1239 lang=python3
#
# [1239] 串联字符串的最大长度
#

# @lc code=start
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        # lengths = [len(word) for word in arr]
        # if max(lengths) == 26:
        #     return 26
        # else:
        #     arr.sort( lambda: x, len(x))
        
        # for i in range(arr)
        
        
        masks = list()
        for s in arr:
            mask = 0
            for ch in s:
                idx = ord(ch) - ord("a")
                if ((mask >> idx) & 1):   # // 若 mask 已有 ch，则说明 s 含有重复字母，无法构成可行解
                    mask = 0
                    break
                mask |= 1 << idx   # 将 ch 加入 mask 中
            if mask > 0:
                masks.append(mask)

        ans = 0

        def backtrack(pos: int, mask: int) -> None:
            if pos == len(masks):
                nonlocal ans
                ans = max(ans, bin(mask).count("1"))
                return
            
            if (mask & masks[pos]) == 0:   # mask 和 masks[pos] 无公共元素
                backtrack(pos + 1, mask | masks[pos])
            backtrack(pos + 1, mask)
        
        backtrack(0, 0)
        return ans

# @lc code=end

