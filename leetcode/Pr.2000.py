class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type ch: str
        :rtype: str
        """
        idx = word.find(ch)
        
        if idx != -1:
            return word[:idx + 1][::-1] + word[idx + 1:]
        else:
            return word
'''
I discovered the function find()
'''