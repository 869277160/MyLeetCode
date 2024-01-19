#
# @lc app=leetcode.cn id=1694 lang=python3
#
# [1694] 重新格式化电话号码
#

# @lc code=start
class Solution:
    def reformatNumber(self, number: str) -> str:
        
        # (1) remove blank and -
        number_1 = number.replace(" ", "").replace("-", "")
        
        # (2) split into parts
        if len(number_1) <= 3:
            return number_1
        elif len(number_1) == 4:
            return number_1[0:2] + "-" + number_1[2:]
        else :
            left = len(number_1) % 3
            all_parts = len(number_1) // 3

        if left ==1:
            all_parts -= 1
            res = ""
            for i in range(all_parts):
                res += number_1[i*3:(i+1)*3] + "-"
            res += number_1[-4:-2] + "-" + number_1[-2:]
            return res 
        
        elif left ==2 :
            res = ""    
            for i in range(all_parts):
                res += number_1[i*3:(i+1)*3] + "-"
            res +=  number_1[-2:]
            return res 
        
        elif left ==0 :
            res = ""
            for i in range(all_parts):
                res += number_1[i*3:(i+1)*3] + "-"
            
            return res[:-1]
            
# @lc code=end

