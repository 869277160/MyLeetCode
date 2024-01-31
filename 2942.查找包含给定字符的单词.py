#
# @lc app=leetcode.cn id=2942 lang=python3
#
# [2942] 查找包含给定字符的单词
#

# @lc code=start
class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        
        return [i for i in range(len(words)) if x in words[i]]



# @lc code=end

