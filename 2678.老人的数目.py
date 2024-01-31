#
# @lc app=leetcode.cn id=2678 lang=python3
#
# [2678] 老人的数目
#

# @lc code=start
class Solution:
    def countSeniors(self, details: List[str]) -> int:
        # print(details[0][11:13])
        user = [1 for detail in details if int(detail[11:13]) > 60]
        return sum(user)
        
        
# @lc code=end

