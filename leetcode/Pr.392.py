class Solution(object):
    def isSubsequence(self, s, t):
        s1, t1 = 0, 0

        while s1 < len(s) and t1 < len(t):
            if s[s1] == t[t1]:
                s1 += 1
            t1 += 1
        return s1 == len(s)

s = Solution()
print(s.isSubsequence("abc", "afbgvc"))
'''
I remembered what pointers are for
I understand better the diference betwin while and for loop
'''