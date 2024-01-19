#
# @lc app=leetcode.cn id=2224 lang=python3
#
# [2224] 转化时间需要的最少操作数
#

# @lc code=start
class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        
        current_hour = int(current[:2])
        current_min  = int(current[3:])
        
        correct_hour = int(correct[:2])
        correct_min  = int(correct[3:])
        
        

        if current_hour == correct_hour:
            if current_min == correct_min:
                return 0
            
            if current_min < correct_min:
                min_diff = correct_min - current_min
                return self.min_tune(min_diff)
            
            elif current_min > correct_min:
                # 调整小时到前一个小时
                res = 23
                # 计算剩余分钟数
                min_diff = 60 -current_min + correct_min
                
                return self.min_tune(min_diff)
        
        elif current_hour > correct_hour:
            if current_min == correct_min:
                return 24
            
            if current_min < correct_min:
                res = 23 - current_hour + correct_hour 
                
                min_diff = correct_min - current_min
                return res + self.min_tune(min_diff)
            
            elif current_min > correct_min:
                # 调整小时到前一个小时
                res = 23 - current_hour + correct_hour 
                # 计算剩余分钟数
                min_diff = 60 - current_min + correct_min
                
                return res + self.min_tune(min_diff)
        
        
        elif current_hour < correct_hour:
            if current_min == correct_min:
                return  correct_hour - current_hour
            
            if current_min < correct_min:
                res = correct_hour - current_hour
                min_diff = correct_min - current_min
                return res + self.min_tune(min_diff)
            
            elif current_min > correct_min:
                # 调整小时到前一个小时
                res = correct_hour - current_hour - 1
                # 计算剩余分钟数
                min_diff = 60 - current_min + correct_min
                
                return res + self.min_tune(min_diff)
    
    def min_tune(self,minute):
        
        res = 0
        res += minute // 15
        minute = minute %15
        
        if minute != 0:
            res += minute // 5
            minute = minute % 5
            return res + minute
        else:
            return res 
        
# @lc code=end

