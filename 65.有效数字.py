#
# @lc app=leetcode.cn id=65 lang=python3
#
# [65] 有效数字
#

# @lc code=start
class Solution:
    def isNumber(self, s: str) -> bool:
        # hasdot = 0 
        # hase = 0 
        # hassign = 0 
        
        # validelem = "0123456789+-.e"
        # validnum = "0123456789"
            
         
        # 循环检测，首先保证特殊符号只有一次，之后通过特殊符号进行分割，对前后部分进行检测
        # 或者可以分开进行检测，即self.isdot ，is fullnum, is fullnumwithe 
        # for i in range(len(s)):
        #     ch = s[i]
            
        #     if ch not in validelem:
        #         return False
        #     else :
        #         if ch == "-" or ch == "+":
        #             if i == 0:
        #                 hassign = hassign + 1
        #             if i != 0 and hassign == 1:
        #                 return False
                
        #         if ch == ".":
        #             hasdot = hasdot + 1
        #             if hasdot == 1:
        #                 return False
                
        #         if ch == ".":
        #             hasdot = hasdot + 1
        #             if hasdot == 1:
        #                 return False
                    
        #         if ch in validnum:
                    
                    
        
        
# @lc code=end

