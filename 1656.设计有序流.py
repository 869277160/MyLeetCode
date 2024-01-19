#
# @lc app=leetcode.cn id=1656 lang=python3
#
# [1656] 设计有序流
#

# @lc code=start
class OrderedStream:

    def __init__(self, n: int):
        self.id_list = [False for i in range(n+1)]
        self.ptr = 1
        # self.next_False = 1
        self.id_dict = {}

    def insert(self, idKey: int, value: str) -> List[str]:
        self.id_list[idKey] = True
        self.id_dict[idKey] = value
        
        if self.ptr != idKey:
            return []
        else :
            res = []
            for i in range(self.ptr,len(self.id_list)):
                if self.id_list[i] == False:
                    self.ptr = i
                    return res
                else:
                    self.ptr = i
                    res.append(self.id_dict[i])
            
            return res 
        
        # res = []
        # for i in range(idKey,len(self.id_list)+1):
        #     if self.id_list[i-1] == False:
        #         self.ptr = i-1
        #         return res
        #         break
        #     else:
        #         self.ptr = i



# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)
# @lc code=end

