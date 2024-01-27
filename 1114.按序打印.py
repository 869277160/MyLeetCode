'''
Author: DingWang wangding19@mails.ucas.ac.cn
Date: 2024-01-25 23:54:06
LastEditors: DingWang wangding19@mails.ucas.ac.cn
LastEditTime: 2024-01-25 23:56:42
FilePath: \Leetcode_Solver\1114.按序打印.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1114 lang=python3
#
# [1114] 按序打印
#

# @lc code=start
class Foo:
    def __init__(self):
        # self.lock1 = True
        self.lock2 = True
        self.lock3 = True
        

    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.lock2 = False
        


    def second(self, printSecond: 'Callable[[], None]') -> None:
        
        while 1:
            if not self.lock2:
            # printSecond() outputs "second". Do not change or remove this line.
                printSecond()
                self.lock3 = False
                break

    def third(self, printThird: 'Callable[[], None]') -> None:
        while 1:
            if not self.lock3:
                # printThird() outputs "third". Do not change or remove this line.
                printThird()
                break
            
# @lc code=end

