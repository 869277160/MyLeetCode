#
# @lc app=leetcode.cn id=139 lang=python3
#
# [139] 单词拆分
#
from functools import cache
# @lc code=start
class Solution:
    def __init__(self) -> None:
        self.memo = []
        self.length = 0
    
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        self.length = len(s)
        self.memo = [-1] * self.length
        
        return self.dp(s,wordDict,0)
    
    def dp(self, s, wordDict, pos) -> bool :
        if pos == self.length:
            return True
        
        if self.memo[pos] != -1:
            return True if self.memo[pos] == 1 else False

        for word in wordDict:
            length = len(word)
            if pos + length > len(s):
                continue
            sub_str = s[pos:pos+length]
            
            if sub_str != word:
                continue
                
            # s[i..] 的前缀被匹配，去尝试匹配 s[i+len..]
            if self.dp(s, pos+length, wordDict):
                # s[i..] 可以被拼出，将结果记入备忘录
                self.memo[pos] = 1
                return True
        
        # s[i..] 不能被拼出，结果记入备忘录
        self.memo[pos] = 0
        return False
        
        
        
        
        
        
        
        
        
        
        
# @lc code=end

