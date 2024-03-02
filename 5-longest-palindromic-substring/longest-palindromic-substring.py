class Solution(object):
    def isPalindrome(self, s, l, r):
        """
        :type s: str
        :rtype: str
        """
        Palindrome = False
        n = len(s)

        while l >= 1 and r <= n - 2:
            if s[l] == s[r]:
                l -= 1
                r += 1
            else: 
                break
        # print (s[l:r+1])
        # print (s[l] == s[r])
        if s[l] == s[r]:
            return s[l:r+1]  
        else:

            return s[l+1:r]
            

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s) 
        if n<=1: return s
        res = ''
        for i in range(n-1):
            res1 = self.isPalindrome(s, i, i)
            res2 = self.isPalindrome(s, i, i+1)
            if len(res1) > len(res):
                res = res1
            if len(res2) > len(res):
                res = res2
        return res 