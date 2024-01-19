'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-10 15:10:17
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-10 15:19:26
FilePath: \Leetcode_Solver\225.用队列实现栈.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=225 lang=python3
#
# [225] 用队列实现栈
#

# @lc code=start
# from collections import deque


class MyStack:
    def __init__(self):
        self.in_quene = []
        # self.out_quene = []
        self.top_elem: int = -1 

    def push(self, x: int) -> None:
        self.in_quene.append(x)
        self.top_elem = x
        # return

    def pop(self) -> int:
        # 获取当前栈中元素个数
        size = len(self.in_quene)
        while size > 1:
            # 将队头元素加入到队尾
            self.in_quene.append(self.in_quene.pop(0))
            size -= 1
            
        # 取出队头元素并返回
        output = self.in_quene.pop(0)
        self.top_elem = self.in_quene[-1] if self.in_quene else -1
        return output

    def top(self) -> int:
        return self.top_elem

    def empty(self) -> bool:
        return self.in_quene == []


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
# @lc code=end

