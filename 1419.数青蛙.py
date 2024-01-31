#
# @lc app=leetcode.cn id=1419 lang=python3
#
# [1419] 数青蛙
#

# @lc code=start
class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        
        res = ["c"]
        for i in range(len(croakOfFrogs)):
            # print(res)
            if croakOfFrogs[i] in "croak":
                res, num = self.update(res, croakOfFrogs[i])
            else:
                return -1

            if num == -1 :
                return -1
        
        return len(res) if res == ["c"]*len(res) else -1
    
    def update(self, res, temp):
        # print(res,temp)
        target = {"c":"r","r":"o","o":"a","a":"k","k":"c"}
        if temp not in target.keys():
            return res, -1 
        else:
            if temp in res:
                res[res.index(temp)] = target[temp]
                return res, 0
            if temp not in res:
                if temp == "c":
                    res.append('r')
                    return res, 0
                else:
                    return res, -1

        
        # for i in range(len(res)):
        #     if target[res[i]] == temp:
        #         if temp == "c":
        #             res[i] = 5
        #             return res
        #         else:
        #             res[i] -= 1 
        #             return res
        #     else:
        #         if temp == "c":
        #             res.append(5)
        #         else:
        #             res[i] = 7
        #             return res 
       
        return res, 0
# @lc code=end

