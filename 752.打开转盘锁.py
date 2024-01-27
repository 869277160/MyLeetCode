'''
Author: DingWang wangding19@mails.ucas.ac.cn
Date: 2024-01-22 15:03:38
LastEditors: DingWang wangding19@mails.ucas.ac.cn
LastEditTime: 2024-01-22 16:23:16
FilePath: \Leetcode_Solver\752.打开转盘锁.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=752 lang=python3
#
# [752] 打开转盘锁
#

from typing import List
from collections import deque

# @lc code=start
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        
        # 记录已经访问过的密码
        visited = set()
        for code in deadends:
            visited.add(code)
        q = deque()
        step = 0
        q.append("0000")
        visited.add("0000")
        
        while q:
            print(q)
            q_size = len(q)
            
            for i in range(q_size):
                # 访问当前密码
                current_code = q.popleft()
                
                # 结束条件
                if current_code == target:
                    return step
                if current_code in deadends:
                    continue
                
                # 在队列中加入相邻节点
                for j in range(4):
                    next_code = self.plusOne(current_code, j)
                    if next_code not in visited:
                        q.append(next_code)
                        visited.add(next_code)
                    next_code = self.minusOne(current_code, j)
                    if next_code not in visited:
                        q.append(next_code)
                        visited.add(next_code)
            step += 1

        return -1
            
        
    def plusOne(self, current_code, j):
        ch = list(current_code)
        if ch[j] == '9':
            ch[j] = '0'
        else:
            ch[j] = str(int(ch[j]) + 1)
        return ''.join(ch)
        
    def minusOne(self, current_code, j):
        ch = list(current_code)
        if ch[j] == '0':
            ch[j] = '9'
        else:
            ch[j] = str(int(ch[j]) - 1)
        return ''.join(ch)
# @lc code=end