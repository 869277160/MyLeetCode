'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-02 10:15:01
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-10 15:09:05
FilePath: \Leetcode_Solver\232.用栈实现队列.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=232 lang=python3
#
# [232] 用栈实现队列
#
# list 作为栈的操作
#  pop  list.pop()
#  push list.append()
#  peek  list[-1]

# @lc code=start
class MyQueue:

    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, x: int) -> None:
        self.in_stack.append(x)

    def pop(self) -> int:
        self.peek()
        return self.out_stack.pop()
    
    def peek(self) -> int:
        if len(self.out_stack) == 0:
            # 把 s1 元素压入 s2
            while len(self.in_stack) != 0:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack[-1]

    def empty(self) -> bool:
        return self.in_stack ==[] and self.out_stack == []


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end

