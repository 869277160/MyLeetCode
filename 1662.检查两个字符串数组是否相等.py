#
# @lc app=leetcode.cn id=1662 lang=python3
#
# [1662] 检查两个字符串数组是否相等
#

# @lc code=start
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        
        return self.list2str(word1) == self.list2str(word2)
        
    def list2str(self, words: List[str]) -> str:
        
        res = ''
        for word in words:
            res += word
        
        return res
        
# @lc code=end

