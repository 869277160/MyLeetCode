#
# @lc app=leetcode.cn id=2744 lang=python3
#
# [2744] 最大字符串配对数目
#

# @lc code=start
class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        res = []
        while(words != []):
            if words[0] not in res:
                if words[0][::-1] in words[1:]:
                    res.append(words[0])
                    res.append(words[0][::-1])

            words = words[1:]
            
            
        return len(res) // 2
        
        
# @lc code=end

