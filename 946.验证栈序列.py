'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-04-07 17:10:16
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-04-07 17:16:41
FilePath: \Leetcode_Solver\946.验证栈序列.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=946 lang=python3
#
# [946] 验证栈序列
#

# @lc code=start
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        if pushed == [] and popped == []:
            return True
        else :
            if len(pushed) != len(popped):
                return False
            
            length = len(pushed)
            
            if pushed == popped :
                return True
            elif pushed == popped[::-1]:
                return True
            else:
                stack = []
                for i in range(length):
                    stack.append(pushed[i])
                    while stack and stack[-1] == popped[0]:
                        print(stack)
                        stack.pop()
                        popped.pop(0)
                        
                if stack==[]:
                    return True
                else :
                    return False

# @lc code=end

