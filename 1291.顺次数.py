#
# @lc app=leetcode.cn id=1291 lang=python3
#
# [1291] 顺次数
#

# @lc code=start
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res = []
        for i in range(1, 10):
            temp = [str(i)]
            for length in range(i+1, 10):
                temp.append(str(length))
                res.append(int("".join(temp)))
        
        temp = []
        res.sort()
        for i in range(len(res)):
            if res[i] >= low and res[i] <= high:
                temp.append(res[i])
        
        return temp
# @lc code=end

