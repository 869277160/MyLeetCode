#
# @lc app=leetcode.cn id=2114 lang=python3
#
# [2114] 句子中的最多单词数
#

# @lc code=start
class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        
        return max([len(s.split()) for s in sentences])
        
        
# @lc code=end

