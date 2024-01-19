#
# @lc app=leetcode.cn id=1603 lang=python3
#
# [1603] 设计停车系统
#

# @lc code=start
class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.max_big_parking_space = big
        self.big_parking_space = [0] * big
        self.big_parking_space_index = 0
        
        self.max_medium_parking_space = medium
        self.medium_parking_space = [0] * medium
        self.medium_parking_space_index = 0
        
        self.max_small_parking_space = small
        self.small_parking_space = [0] * small
        self.small_parking_space_index = 0

    def addCar(self, carType: int) -> bool:
        if carType == 1:
            if self.big_parking_space_index >= self.max_big_parking_space:
                return False
            else :
                self.big_parking_space.append(1)
                self.big_parking_space_index += 1
                return True
        
        elif carType == 2 :
            if self.medium_parking_space_index >= self.max_medium_parking_space:
                return False
            else :
                self.medium_parking_space.append(2)
                self.medium_parking_space_index += 1
                return True
            
        elif carType ==3:
            if self.small_parking_space_index >= self.max_small_parking_space:
                return False
            else :
                self.small_parking_space.append(3)
                self.small_parking_space_index += 1
                return True 
        
        else:
            return False 



# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
# @lc code=end

