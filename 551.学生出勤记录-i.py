#
# @lc app=leetcode.cn id=551 lang=python3
#
# [551] 学生出勤记录 I
#

# @lc code=start
class Solution:
    def checkRecord(self, s: str) -> bool:
        res_dict = {"A":0, 
                    "L":0, 
                    "P":0,}
        
        for i in range(0,len(s)):
            res_dict[s[i]] +=1
            if res_dict["A"] >= 2 :
                return False 
            if s[i-2:i+1] == "LLL" or s[i-1:i+2] == "LLL" or s[i:i+3] == "LLL":
                return False 
        
        return True
# @lc code=end

