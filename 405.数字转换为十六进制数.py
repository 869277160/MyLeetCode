#
# @lc app=leetcode.cn id=405 lang=python3
#
# [405] 数字转换为十六进制数
#

# @lc code=start
class Solution:
    def toHex(self, num: int) -> str:
       
        uniqueelem="0123456789abcdef"
        if num >= 0:
            if num < 16:
                return uniqueelem[num]
            else:
                res = ""
                while num:
                    res = uniqueelem[num % 16] + res
                    num = num // 16
                return res 
        else :
            if num > -17:
                return "fffffff" + uniqueelem[16+num]
            else:
                out = -num
                res = ""
                adder = 0
                while out:
                    res = uniqueelem[-(out % 16) - adder] + res
                    if out % 16 != 0:
                        adder = 1
                    out = out // 16
                return "f"*(8-len(res)) +res 
                
                
            # if num == -1 :
            #     return 
            # if num == -2 :
            #     return "fffffffe"
        
            return res
# @lc code=end

