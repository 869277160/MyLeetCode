#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
#

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        self.memo = [-666] * (amount + 1)
        return self.dp(coins, amount)

    def dp(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        if amount < 0:
            return -1
        # 查备忘录，防止重复计算
        if self.memo[amount] != -666:
            return self.memo[amount]

        res = float("inf")
        for coin in coins:
            # 计算子问题的结果
            sub_problem = self.dp(coins, amount - coin)
            # 子问题无解则跳过
            if sub_problem == -1:
                continue
            # 在子问题中选择最优解，然后加一
            res = min(res, sub_problem + 1)

        # 把计算结果存入备忘录
        self.memo[amount] = -1 if res == float("inf") else res
        return self.memo[amount]
        
# @lc code=end

