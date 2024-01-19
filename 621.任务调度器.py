'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-17 16:08:24
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-17 16:30:00
FilePath: \Leetcode_Solver\621.任务调度器.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=621 lang=python3
#
# [621] 任务调度器
#

# @lc code=start
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        res = len(tasks)

        if n == 0 :
            return res 
        
        else :
            
            import collections
            # 收集所有的任务的出现次数{任务：次数}
            all_counter = collections.Counter(tasks)
            # 找到出现次数最多的任务所对应的次数
            max_time = max(all_counter.values())
            # 找到这些任务的个数有多少
            max_count = list(all_counter.values()).count(max_time)
            
            # 按照出现最多次数的任务，计算出最少的执行次数
            # max_time - 1 为最后一次执行的任务后面不需要对应的冷却时间
            # 每次执行的任务数为 n + 1， 加一代表当前任务
            res = (max_time - 1) * (n + 1) 
            # 最后加入出现次数最多的任务的个数
            # 因为一次执行任务需要把这些任务都执行一遍
            res +=  max_count
            
            
            # 但是, 如果最后的结果小于任务的总数，那么就返回任务的总数
            # 存在一种情况，
            # 即 仅针对出现次数最多的任务进行安排时，可能无法考虑剩余任务出现的任务总数大于最多数任务能够cover的情况
            return res if res >= len(tasks) else len(tasks)
        
# @lc code=end

