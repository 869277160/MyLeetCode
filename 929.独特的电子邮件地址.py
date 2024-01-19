#
# @lc app=leetcode.cn id=929 lang=python3
#
# [929] 独特的电子邮件地址
#

# @lc code=start
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:

        res = {}
        
        for email in emails:
            name,home = email.split("@")
            items = name.split('+')[0].split(".")
            realemail = "@" + home
            for item in items[::-1]:
                realemail =  item + realemail 
            
            res[realemail] =1
            
        return len(res.keys( ))
        
# @lc code=end

