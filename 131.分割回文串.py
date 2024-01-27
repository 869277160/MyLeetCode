#
# @lc app=leetcode.cn id=131 lang=python3
#
# [131] 分割回文串
#

# @lc code=start
class Solution:
    def partition(self, s: str) -> List[List[str]]:
            self.isPalindrome = lambda s : s == s[::-1]
            res = []
            self.backtrack(s, res, [])
            return res
        
    def backtrack(self, s, res, path):
        if not s:
            res.append(path)
            return
        for i in range(1, len(s) + 1): #注意起始和结束位置
            if self.isPalindrome(s[:i]):
                self.backtrack(s[i:], res, path + [s[:i]])
    # def partition(self, s: str) -> List[List[str]]:
    #     # if s == "":
    #     #     return []
    #     # if len(s) == 1:
    #     #     return [[s]]
    #     self.is_rev = lambda s : s == s[::-1]
        
    #     res = []
    #     self.traverse(s, res, [])
    #     return res 
    
    # def traverse(self, rest, res, track):
    #     print(rest, track, res)

    #     if not rest:
    #         res.append(track)
    #         return
    #     else:
    #         for i in range(1,len(rest)+1):
    #             if self.is_rev(rest[:i]):
    #                 self.traverse(rest[i:], res, track + [rest[:i]])

    # def is_rev(self, s:str) -> bool:
        
    #     if s == s[::-1]:
    #         return True
    #     else:
    #         return False
        

# @lc code=end

