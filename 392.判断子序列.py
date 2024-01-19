#
# @lc app=leetcode.cn id=392 lang=python3
#
# [392] 判断子序列
#

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # 两次遍历求解
        for i in range(len(s)):
            if s[i] in t:
                t = t[t.index(s[i])+1:]
            else:
                return False
        
        # 二维动态规划求解
        # 上下三角dp table 求解
        # 画图即可
        # dp: list[list[bool]] = [[False for _ in range(len(t)+1)] for _ in range(len(s)+1)]
        # # 
        # # for i in range(len(s)+1):
        # dp[0][0] = (s[0] == t[0])
            
        # for i in range(0,len(s)):
        #     for j in range(i+1,len(t)):
        #         dp[i][j] = dp[i-1][j-1] or (dp[i][j-1] or s[i] == t[j])
                
        # print(dp)
        # return dp[-1][-1]


        
        
# @lc code=end

