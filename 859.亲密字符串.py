#
# @lc app=leetcode.cn id=859 lang=python3
#
# [859] 亲密字符串
#

# @lc code=start
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False 

        # 暴力求解方法
        # for i in range(len(s)):
        #     for j in range(i+1,len(s)):
        #         if s[i] == goal[j] and s[j] == goal[i]:
        #             if s[:i] + s[j] + s[i+1:j] + s[i] + s[j+1:] == goal:
        #                 return True
        # return False

        # 由于必须交换一次，在相同的情况下，交换相同的字符
        if s == goal and len(set(s)) < len(goal): return True
        
        # 使用 zip 进行匹配对比，挑出不同的字符对
        dif = [(a, b) for a, b in zip(s, goal) if a != b]
        
        # 对数只能为2，并且对称，如 (a,b)与(b,a)
        return len(dif) == 2 and dif[0] == dif[1][::-1]
  
        
# @lc code=end

