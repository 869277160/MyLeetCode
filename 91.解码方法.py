#
# @lc app=leetcode.cn id=91 lang=python3
#
# [91] 解码方法
#

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        f = [1] + [0] * n
        for i in range(1, n + 1):
            if s[i - 1] != '0':
                f[i] += f[i - 1]
            if i > 1 and s[i - 2] != '0' and int(s[i-2:i]) <= 26:
                f[i] += f[i - 2]
        return f[n]

    # def numDecodings(self, s: str) -> int:
    #     str_len = len(s)
    #     self.mapper = {}
    #     for i in range(1,27):
    #         if i < 10:
    #             self.mapper[str(i)] = 1
    #         elif i == 10 or i == 20 :
    #             self.mapper[str(i)] = 1
    #         else :
    #             self.mapper[str(i)] = 2
    #     res = 0
        
    #     res = self.DecodingSolver(s,res)
            
    #     return res 
        
      
        
    # def DecodingSolver(self, input_s:str,res:int):
    #     # print(s)
    #     # 判断结束条件
    #     if len(input_s) == 0 or input_s[0] == "0":
    #         return 0 
    #     elif input_s in self.mapper.keys():
    #         return self.mapper[input_s]
    #     else :
    #         # 一次走两步的时候如何走
    #         inputer = input_s[:2]
    #         if inputer in self.mapper.keys():
    #             res += self.DecodingSolver(input_s[2:], 0) # type: ignore
    #         else:
    #             res +=  0

    #         # 一次走一步的时候如何走
    #         inputer = input_s[:1]
    #         if inputer in self.mapper.keys():
    #             res += self.DecodingSolver(input_s[1:],0)
    #         else:
    #             res +=  0
    #         return res
        
# @lc code=end


if __name__ == "__main__":

    s = Solution()
    print(s.numDecodings("11106"))