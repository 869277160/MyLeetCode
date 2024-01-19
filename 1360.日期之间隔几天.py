#
# @lc app=leetcode.cn id=1360 lang=python3
#
# [1360] 日期之间隔几天
#

# @lc code=start
class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        
        # start_year = max(int(date1[:4]),int(date2[:4]))
        # end_year = min(int(date1[:4]),int(date2[:4]))
        
        # start_month = max(int(date1[5:7]),int(date2[5:7]))
        # end_month = min(int(date1[5:7]),int(date2[5:7]))
        
        # start_day = max(int(date1[8:]),int(date1[8:]))
        # end_day = min(int(date1[8:]),int(date2[8:]))
        
        # # 同年
        # if start_year == end_year:
        #     # 同月
        #     if start_month == end_month:
        #         return abs(start_day - end_day)
        #     # 不同月
        #     else:
        #         month_of_the_year = [31,28,31,30,31,30,31,31,30,31,30,31]
        #         if start_year % 4 == 0 and start_year % 100 != 0 or start_year % 400 == 0:
        #             month_of_the_year[1] = 29
                    
        #         return abs(start_day - end_day) + sum[]
        
        import datetime
        
        return abs((datetime.datetime.strptime(date1, "%Y-%m-%d") - datetime.datetime.strptime(date2, "%Y-%m-%d")).days)
        
        
        
        
# @lc code=end

