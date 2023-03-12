#
# @lc app=leetcode.cn id=1974 lang=python3
#
# [1974] 使用特殊打字机键入单词的最少时间
#

# @lc code=start
class Solution:
    def minTimeToType(self, word: str) -> int:
        
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        alphabet_dict = {alphabet[i]:i for i in range(26)}
        
        
        res = 0
        current_p = 0
        for i in word:
            # 选择正转或者反转中最小的一个
            res += min(abs(alphabet_dict[i] - current_p), 26 - abs(alphabet_dict[i] - current_p))
            
            # return res 
            # 转到特定位置
            current_p = alphabet.index(i)
            
            # 输入
            res +=1 
        
        
        return res
        
# @lc code=end

