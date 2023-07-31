class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor = x ^ y
        cnt = 0
        while xor:
            if xor & 1:
                cnt += 1
            xor >>= 1
            
        return(cnt)
