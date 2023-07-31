class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        import math

        if (n < 0) or (n==0):
            return False
        
        if math.log(n, 4).is_integer():
            return True

        return False
