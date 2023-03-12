#
# @lc app=leetcode.cn id=2269 lang=python3
#
# [2269] 找到一个数字的 K 美丽值
#

# @lc code=start
class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        
        str_num = str(num)
        total_len =len(str_num)
        
        res = 0
        for i in range(0,total_len-k+1):
            if int(str_num[i:i+k]) != 0 and num % int(str_num[i:i+k]) == 0:
                    res += 1 
                
        return res 
        
        
        
# @lc code=end

