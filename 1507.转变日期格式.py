#
# @lc app=leetcode.cn id=1507 lang=python3
#
# [1507] 转变日期格式
#

# @lc code=start
class Solution:
    def reformatDate(self, date: str) -> str:
        
        day, month, year = date.split(' ')
        
        Month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        month = Month.index(month) + 1
        day = day[:-2]
        
        if month < 10:
            month = "0" + str(month)
        if len(day) <2:
            day = "0" + day
            
        res = f"{year}-{month}-{day}"
        
        return res 
        
# @lc code=end

