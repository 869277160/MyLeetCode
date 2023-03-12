#
# @lc app=leetcode.cn id=278 lang=python3
#
# [278] 第一个错误的版本
#

# @lc code=start
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        if isBadVersion(1) == True:
            return 1 
        if n == 2:
            return 1 if isBadVersion(1) else 2 
        if n == 3 :
            if isBadVersion(2):
                return 1 if isBadVersion(1) else 2
            else :
                return 3
        if isBadVersion(n) == True and isBadVersion(n-1) == False:  return n

        
        def helper(max, min, current):
            # 头部和尾部
            if max == 1: return 1
            if min == n: return n
            
            # 结束递归
            if isBadVersion(current) == True and isBadVersion(current-1) == False:
                return current
            
            # 正在 错误区
            elif isBadVersion(current) == True and isBadVersion(current-1) == True:
                current_max = current
                current_min = min
                currenter = (current_max+current_min) //2
                return helper(current_max, current_min, currenter)
                
            # 正在 良好区
            elif isBadVersion(current) == False and isBadVersion(current-1) == False:
                current_max = max
                current_min = current
                currenter = (current_max+current_min) //2
                return helper(current_max, current_min, currenter)
            
            # 正在外太空。。。。
            elif isBadVersion(current) == False and isBadVersion(current-1) == True:
                return 

        return helper(n, 1, (n) // 2)
# @lc code=end

