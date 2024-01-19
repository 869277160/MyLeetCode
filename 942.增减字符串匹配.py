#
# @lc app=leetcode.cn id=942 lang=python3
#
# [942] 增减字符串匹配
#

# @lc code=start
class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        
        if s == "I":
            return [0,1]
        elif s == "D":
            return [1,0]
        elif s == "II":
            return [0,1,2]
        elif s == "ID":
            return [0,2,1]
        elif s == "DD":
            return [2,1,0]
        elif s == "DI":
            return [2,0,1]
        else:
            total = len(s)
            
            if s == "I"*len(s):
                return [i for i in range(total+1)]
            if s == "D"*len(s):
                return [i for i in range(total,-1,-1)]
            
            
            
            res = [0] if s[0] == "I" else [total]
            current_I = 1 if s[0] == "I" else 0
            current_D = total-1 if s[0] == "D" else total
            for i in s[1:]:
                if i == "I":
                    res.append(current_I)
                    current_I += 1
                else:
                    res.append(current_D)
                    current_D -= 1
            
            res += [current_I] if s[-1] == "I" else [current_D]
                
            return res
            
        
# @lc code=end

