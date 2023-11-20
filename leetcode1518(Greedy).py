# Water Bottles
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        result = numBottles

        while True:
            mod = numBottles % numExchange
            numBottles = (numBottles // numExchange)
            result += numBottles
            if numBottles + mod < numExchange:
                break
            else:
                numBottles = numBottles + mod
        
        return result