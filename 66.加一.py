#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        char_digits=""
        for i in range(0,len(digits)):
            char_digits+=str(digits[i])
        res=int(char_digits)
        res+=1
        res_char=str(res)
        res_list=[]
        for i in range(0,len(res_char)):
            res_list.append(int(res_char[i]))
        return res_list

# @lc code=end

