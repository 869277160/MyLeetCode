'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-21 09:42:03
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-21 09:49:45
FilePath: \Leetcode_Solver\1299.将每个元素替换为右侧最大元素.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1299 lang=python3
#
# [1299] 将每个元素替换为右侧最大元素
#

# @lc code=start
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        if len(arr) == 1:
            return [-1]
        
        else :
            # 直接用max()函数会超时
            # 改成遍历时候逐步替换即可
            current_max = max(arr[1:])
            arr[0] = current_max
            for i in range(1,len(arr)-1):
                if arr[i] == current_max:
                    arr[i] = max(arr[i+1:])
                    current_max = arr[i]
                else:
                    arr[i] = current_max
                    
            
            arr[-1] = -1
            
            return arr
        
# @lc code=end

