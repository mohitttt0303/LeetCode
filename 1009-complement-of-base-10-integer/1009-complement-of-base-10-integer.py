class Solution(object):
    def bitwiseComplement(self, n):
        if n == 0:
            return 1
        
        mask = 0
        temp = n
        
        # create mask like 111...
        while temp > 0:
            mask = (mask << 1) | 1
            temp >>= 1
        
        return mask ^ n