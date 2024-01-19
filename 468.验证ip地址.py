#
# @lc app=leetcode.cn id=468 lang=python3
#
# [468] 验证IP地址
#

# @lc code=start
class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        if queryIP.find(".") == -1 and queryIP.find(":") == -1:
            return "Neither"
        elif queryIP.find(".") != -1 and queryIP.find(":") != -1:
            return "Neither"
        elif queryIP.find(".") != -1 and queryIP.find(":") == -1:
            if queryIP.count(".") != 3:
                return "Neither"
            else:
                ip_list = queryIP.split(".")
                for ip in ip_list:
                    if ip == "":
                        return "Neither"
                    if ip[0] == "0" and len(ip) > 1:
                        return "Neither"
                    if ip[0] == "-":
                        return "Neither"
                    if not ip.isdigit():
                        return "Neither"
                    if int(ip) > 255:
                        return "Neither"
                return "IPv4"
        elif queryIP.find(".") == -1 and queryIP.find(":") != -1:
            def isIPv6(ip: str) -> bool:
                return all(s and len(s) <= 4 and all(c in "0123456789ABCDEFabcdef" for c in s) for s in sp) if len(sp := ip.split(":")) == 8 else False

            if isIPv6(queryIP):
                return "IPv6"
            else:
                return "Neither"
       


# @lc code=end

