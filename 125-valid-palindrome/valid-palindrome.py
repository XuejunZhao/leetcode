class Solution:
    def isPalindrome(self, s: str) -> bool:
        arr = []
        for c in s:
            if c.islower() or c.isdigit(): 
                arr.append(c)
            elif c.isupper(): 
                arr.append(c.lower())
            
        # print (arr)
        l = 0 
        r = len(arr) -1
        while l < r: 
            if arr[l] == arr[r]:
                l += 1
                r -= 1
            else: 
                # print (l, arr[l])
                # print (r, arr[r])
                return False 
        return True