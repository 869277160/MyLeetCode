#
# @lc app=leetcode.cn id=2960 lang=python3
#
# [2960] 统计已测试设备
#

# @lc code=start
class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        
        # minus_percent = [0 for _ in batteryPercentages]
        # res = 1 if batteryPercentages[0] > 0 else 0
        # minus_percent[0] = 1 if batteryPercentages[0] > 0 else 0
        # for i in range(1,len(batteryPercentages)):
        #     if batteryPercentages[i] > minus_percent[i-1]:
        #         res += 1 
        #         minus_percent[i] = minus_percent[i-1] + 1
        #     else :
        #         minus_percent[i] = minus_percent[i-1]
        
        # return res 
        
        # minus_percent = [0 for _ in batteryPercentages]
        res = 1 if batteryPercentages[0] > 0 else 0
        # minus_percent[0] = 1 if batteryPercentages[0] > 0 else 0
        for i in range(1,len(batteryPercentages)):
            # print(res)
            if batteryPercentages[i] > res:
                res += 1 
                # minus_percent[i] = minus_percent[i-1] + 1
            # else :
            #     minus_percent[i] = minus_percent[i-1]
        
        return res 
        
        
        
# @lc code=end

