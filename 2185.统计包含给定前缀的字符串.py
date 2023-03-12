#
# @lc app=leetcode.cn id=2185 lang=python3
#
# [2185] 统计包含给定前缀的字符串
#

# @lc code=start
class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        
        count =0
        for word in words:
            if word.find(pref) == 0:
                count +=1
        
        
        return count 
# @lc code=end

