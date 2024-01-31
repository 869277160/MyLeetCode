#
# @lc app=leetcode.cn id=917 lang=python3
#
# [917] 仅仅反转字母
#

# @lc code=start
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        
        left = 0
        right = len(s)-1
        res = [c for c in s]
        while(left < right):
            print(left, right)
            if res[left].isalpha() and res[right].isalpha():
                res[left], res[right] = res[right], res[left]
                left += 1
                right -= 1
            elif res[left].isalpha():
                right -= 1
            elif res[right].isalpha():
                left += 1
            else:
                left += 1
                right -= 1
        return "".join(res)
        
# @lc code=end

