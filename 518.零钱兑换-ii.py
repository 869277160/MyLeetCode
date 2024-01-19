#
# @lc app=leetcode.cn id=518 lang=python3
#
# [518] 零钱兑换 II
#

# @lc code=start
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp_table = []
        for i in range(len(coins)+1):
            dp_table.append([0 for _ in range(amount+1)])
            
        # for i in range(len(coins)+1):
            dp_table[i][0] = 1
        
        for i in range(1,len(coins)+1):
            for j in range(1, amount+1):
                if j-coins[i-1] >=0:
                    dp_table[i][j] = dp_table[i-1][j] + dp_table[i][j-coins[i-1]]
                else:
                    dp_table[i][j] = dp_table[i-1][j]
                    
        print(dp_table)
        return dp_table[-1][-1]
        
        
        
        
        # n = len(coins)
        # dp = [[0]*(amount + 1) for i in range(n+1)]
        # # base case
        # for i in range(n+1):
        #     dp[i][0] = 1

        # for i in range(1, n+1):
        #     for j in range(1, amount+1):
        #         if j - coins[i-1] >= 0:
        #             dp[i][j] = dp[i - 1][j] + dp[i][j - coins[i-1]]
        #         else:
        #             dp[i][j] = dp[i - 1][j]
        # print(dp)
        # return dp[n][amount]
# @lc code=end

