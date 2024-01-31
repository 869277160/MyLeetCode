#
# @lc app=leetcode.cn id=2409 lang=python3
#
# [2409] 统计共同度过的日子数
#

# @lc code=start
class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        arriveAlice_month = int(arriveAlice[:2])
        arriveAlice_allday = sum(months[:arriveAlice_month-1]) +int(arriveAlice[3:])
        leaveAlice_month = int(leaveAlice[:2])
        leaveAlice_allday = sum(months[:leaveAlice_month-1]) +int(leaveAlice[3:])
        
        arriveBob_month = int(arriveBob[:2])
        arriveBob_allday = sum(months[:arriveBob_month-1]) +int(arriveBob[3:])
        leaveBob_month = int(leaveBob[:2])
        leaveBob_allday = sum(months[:leaveBob_month-1]) +int(leaveBob[3:])
        
        print(arriveAlice_allday, leaveAlice_allday, arriveBob_allday, leaveBob_allday)
        
        min_day = min(arriveAlice_allday, arriveBob_allday)
        max_day = max(leaveAlice_allday, leaveBob_allday)
        
        # if arriveBob_allday >= arriveAlice_allday and arriveBob_allday < leaveAlice_allday:
        #     return True 
        # if arriveAlice_allday >= arriveBob_allday and  arriveAlice_allday < leaveBob_allday:
        #     return True 
        
        res = 0
        for day in range(min_day, max_day+1):
          if arriveAlice_allday <= day and arriveBob_allday <= day and \
           leaveBob_allday >= day and leaveAlice_allday >= day:
                res += 1
        

        
        return res 
        
        
        
# @lc code=end

