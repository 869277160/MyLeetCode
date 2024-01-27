'''
Author: DingWang wangding19@mails.ucas.ac.cn
Date: 2024-01-25 17:33:55
LastEditors: DingWang wangding19@mails.ucas.ac.cn
LastEditTime: 2024-01-25 17:54:09
FilePath: \Leetcode_Solver\306.累加数.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=306 lang=python3
#
# [306] 累加数
#

# @lc code=start
class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        if len(num) < 3:
            return False 
        if len(num) == 3:
            return True if int(num[0]) + int(num[1]) == int(num[-1]) else False
            
        
        for i in range(1,len(num)-1):
            if len(num[:i]) > 1 and num[0] == "0":
                break
                
            current_num = int(num[:i])
            if self.traverse(num[i:], current_num):
                return True 
        
        return False 
    
    def traverse(self, num, current_num):
        # print(num)
        for i in range(1,len(num)-1):
            if len(num[:i]) > 1 and num[0] == "0":
                break
            now_num = int(num[:i])
            output = current_num + now_num
            next_num = int(num[i:i+len(str(output))])
            print(current_num, now_num, output, next_num)
            if output == next_num:
                if self.check_rest(num[i+len(str(output)):], now_num, output):
                    return True
        return False 
    
    def check_rest(self, num, now_num, output):
        
        current_idx = 0
        last_num_1 = now_num
        last_num_2 = output
        new_output = last_num_1 + last_num_2
        while current_idx < len(num):
            new_output = last_num_1 + last_num_2
            if str(new_output) != num[current_idx : current_idx + len(str(new_output))]:
                return False
            current_idx = current_idx + len(str(new_output))
            last_num_1 = last_num_2
            last_num_2 = new_output
        return True
    
# @lc code=end

# The line `# print(num)` is commented out, which means it is not executed when the code runs.
# It is used for debugging purposes to print the value of the `num` variable at that point in
# the code. By printing the value of `num`, you can check if the traversal of the number is
# working correctly.
