#
# @lc app=leetcode.cn id=2899 lang=python3
#
# [2899] 上一个遍历的整数
#

# @lc code=start
class Solution:
    def lastVisitedIntegers(self, words: List[str]) -> List[int]:
        res = []
        k = 0
        nums = []
        for i in range(len(words)):
            print(i, nums, k, res)
            if words[i] != "prev":
                nums.append(int(words[i]))
                k = 0
            else :
                if k < len(nums):
                    res.append(nums[::-1][k])
                else :
                    res.append(-1)
                k+=1
        return res 
        
        
        
# @lc code=end

