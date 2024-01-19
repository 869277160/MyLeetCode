#
# @lc app=leetcode.cn id=345 lang=python3
#
# [345] 反转字符串中的元音字母
#

# @lc code=start
class Solution:
    def reverseVowels(self, s: str) -> str:
        VOWELS = "aeiouAEIOU"
        all_vowels = [i for i in s if i in VOWELS]
        
        current_pos = len(all_vowels) - 1
        for i in range(len(s)):
            if s[i] in VOWELS:
                s = s[:i] + all_vowels[current_pos] + s[i+1:]
                current_pos -= 1
        
        # print(s)
        
        return s 
        
        
# @lc code=end

