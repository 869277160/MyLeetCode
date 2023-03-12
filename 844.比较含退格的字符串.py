#
# @lc app=leetcode.cn id=844 lang=python3
#
# [844] 比较含退格的字符串
#

# @lc code=start
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        def helper(s):
            i = 0
            while (i<len(s)):
                if s[i] == "#":
                    if i == 0:
                        s = s[1:]
                    else:
                        s = s[:i-1] + s[i+1:]
                        i -= 1
                else :
                    i+=1    
            return s 
        
        return helper(s) == helper(t)
        
# @lc code=end

