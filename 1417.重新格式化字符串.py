#
# @lc app=leetcode.cn id=1417 lang=python3
#
# [1417] 重新格式化字符串
#

# @lc code=start
class Solution:
    def reformat(self, s: str) -> str:
        
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        nums = "0123456789"

        
        all_nums = [i for i in s if i in nums]
        all_alphabet = [i for i in s if i in alphabet]
        # print(all_nums,all_alphabet)
        if abs(len(all_nums) - len(all_alphabet)) <= 1:
            res = ""
            if len(all_alphabet) > len(all_nums):
                for i in range(len(all_nums)):
                    res += all_alphabet[i] + all_nums[i]
                res += all_alphabet[-1]

            elif len(all_alphabet) < len(all_nums):
                for i in range(len(all_alphabet)):
                    res +=  all_nums[i] + all_alphabet[i]
                res += all_nums[-1]

            elif len(all_alphabet) == len(all_nums):
                res = ""
                for i in range(len(all_nums)):
                    res += all_alphabet[i] + all_nums[i]
            
            
            return res
        else:
            return ""
# @lc code=end

