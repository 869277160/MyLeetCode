'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-20 21:10:45
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-20 21:22:12
FilePath: \Leetcode_Solver\933.最近的请求次数.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=933 lang=python3
#
# [933] 最近的请求次数
#

# @lc code=start
class RecentCounter:

    def __init__(self):
        self.ping_list = []
        

    def ping(self, t: int) -> int:

        
        # count = 1
        def get_new_queue(p_list):
            for i in range(len(p_list)-1,-1,-1):
                if p_list[i] < t - 3000:
                    return p_list[i+1:]
            return p_list
        self.ping_list += [t]
        self.ping_list = get_new_queue(self.ping_list)
        
        # print(self.ping_list)
        return len(self.ping_list)



# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
# @lc code=end

