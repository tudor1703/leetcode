class Solution(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        if n == 1:
            return True
        
        # Divide n by 2, 3, and 5 as long as possible
        for factor in [2, 3, 5]:
            while n % factor == 0:
                n //= factor
        
        # After dividing by 2, 3, and 5, if n becomes 1, it is ugly
        return n == 1
    
s = Solution()
print(s.isUgly(14))
print(s.isUgly(30))
