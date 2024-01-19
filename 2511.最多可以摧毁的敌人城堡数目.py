#
# @lc app=leetcode.cn id=2511 lang=python3
#
# [2511] 最多可以摧毁的敌人城堡数目
#

# @lc code=start
class Solution:
    def captureForts(self, forts: List[int]) -> int:
        if 1 not in forts or -1 not in forts:
            return 0
        
        
        res = 0
        for i in range(len(forts)):
            if forts[i] == 1:
                res = max(max(self.leftsearch(forts[:i]),self.rightsearch(forts[i+1:])),res)
        
        return res
    
    def leftsearch(self,forts):
        if forts == []:
            return 0
        if -1 not in forts or 0 not in forts:
            return 0
        
        for i in range(len(forts)-1,-1,-1):
            if forts[i] == 1:
                return 0
            if forts[i] == -1:
                return len(forts) - i -1
        
        return 0
            
    def rightsearch(self,forts):
        if forts == []:
            return 0
        if -1 not in forts or 0 not in forts:
            return 0

        for i in range(len(forts)):
            if forts[i] == 1:
                return 0
            if forts[i] == -1:
                return i
            
        return 0 
# @lc code=end

