#
# @lc app=leetcode.cn id=2928 lang=python3
#
# [2928] 给小朋友们分糖果 I
#

# @lc code=start
class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        res =0 
        for i in range(0, limit+1):
            for j in range(0, limit+1):
                print(i,j,n - i - j)
                if n - i - j <= limit and n - i - j >= 0:
                    res +=1
        return res
    
    
    #    self.res = 0
    #     self.traverse([], n, limit)
        
    #     return self.res
    
    # def traverse(self, track, all_candy, limit):
    #     print(track)
    #     if len(track) == 3:
    #         self.res += 1
    #         return
        
    #     for i in range(limit+1):
    #         if all_candy - sum(track) >= i:
    #             self.traverse(track+[i], all_candy, limit)
        
# @lc code=end

