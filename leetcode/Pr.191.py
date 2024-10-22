class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        sum = 0
        binary_representation = bin(n)[2:]
        for num in binary_representation:
            sum += int(num)
        return sum

s = Solution()
solved = s.hammingWeight(2147483645)
print(solved)

'''
it's a simple problem,
but after I noticed that 
it could be done even simpler 
with count()
'''
        