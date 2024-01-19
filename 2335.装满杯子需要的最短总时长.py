#
# @lc app=leetcode.cn id=2335 lang=python3
#
# [2335] 装满杯子需要的最短总时长
#

# @lc code=start
class Solution:
    def fillCups(self, amount: List[int]) -> int:
        
        # 优先队列
        # 优先处理数量最多的杯子
        max_amount = max(amount)
        amount.remove(max_amount)
        rest= sum(amount) - max_amount
        if rest <= 0 :
            return max_amount
        else:
            rest = rest // 2 + rest % 2
            return max_amount + rest
        
        
# @lc code=end

