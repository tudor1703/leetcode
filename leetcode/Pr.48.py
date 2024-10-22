class Solution:
    def permute(self, nums):
        if len(nums) == 1:
            return [nums]
        
        result = []
        for i in range(len(nums)):
            current = nums[i]
            remaining = nums[:i] + nums[i+1:]
            for p in self.permute(remaining):  
                result.append([current] + p)
        
        return result

nums = [1,2,3] 
s = Solution()
print(s.permute(nums))
'''
I remembered that recursion is 
often used for factorial type problems
'''