#
# @lc app=leetcode.cn id=500 lang=python3
#
# [500] 键盘行
#

# @lc code=start
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        uniq1 = "qwertyuiop" + "QWERTYUIOP"
        uniq2 = "asdfghjkl" + "ASDFGHJKL"
        uniq3 = "zxcvbnm" + "ZXCVBNM"
        
        res = []
        for word in words:
            if self.Checker(word,uniq1) or self.Checker(word,uniq2) or self.Checker(word,uniq3):
                res.append(word) 
        
        return res 

    def Checker(self,word,unique):
        for i in word:
            if i not in unique:
                return False 
        
        return True

        
# @lc code=end

