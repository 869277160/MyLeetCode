#
# @lc app=leetcode.cn id=93 lang=python3
#
# [93] 复原 IP 地址
#

# @lc code=start
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        if len(s) == 4:
            return [".".join([s[i] for i in range(len(s))])]
        
        self.res = []
        for i in range(1,4):
            now_num = s[:i]
            if len(now_num) > 1 and now_num[0] == "0":
                break
            if int(now_num) > 255:
                    break
            self.traverse(s[i:], [s[:i]])
        return self.res 
    def traverse(self, rest, track):
        print(rest, track, self.res)
        if len(track) == 4:
            if rest == "":
                temp = ".".join(track)
                if temp not in self.res:
                    self.res.append(temp)
            return
        elif len(track) < 4:
            for i in range(1,4):
                now_num = rest[:i]
                if now_num == "":
                    return 
                if len(now_num) > 1 and now_num[0] == "0":
                    break
                if int(now_num) > 255:
                    break
                self.traverse(rest[i:], track + [now_num])
                
        elif len(track) > 4:
            return 
            
# @lc code=end

