#
# @lc app=leetcode.cn id=2243 lang=python3
#
# [2243] 计算字符串的数字和
#

# @lc code=start
class Solution:
    def digitSum(self, s: str, k: int) -> str:
        # print(s, k)
        if len(s) <= k:
                return s
        else :
            temp_res = [int(c) for c in s]
            temp_res_str = ""
            for i in range(0, len(temp_res), k):
                # print(temp_res[i:i+k])
                total = sum(temp_res[i:i+k])
                temp_res_str += str(total)
            
            return self.digitSum(temp_res_str, k)
            
            
# @lc code=end

