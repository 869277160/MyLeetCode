'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2024-01-16 14:19:52
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2024-01-18 14:51:08
FilePath: \Leetcode_Solver\2591.将钱分给最多的儿童.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2591 lang=python3
#
# [2591] 将钱分给最多的儿童
#

# @lc code=start
class Solution:
    def distMoney(self, money: int, children: int) -> int:
        
        money -= children  # 每人至少 1 美元
        if money < 0: return -1
        ans = min(money // 7, children)  # 初步分配，让尽量多的人分到 8 美元
        money -= ans * 7
        children -= ans
        # children == 0 and money：必须找一个前面分了 8 美元的人，分配完剩余的钱
        # children == 1 and money == 3：不能有人恰好分到 4 美元
        if children == 0 and money or \
           children == 1 and money == 3:
            ans -= 1
        return ans

        
# @lc code=end

