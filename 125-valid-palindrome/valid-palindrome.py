class Solution(object):
    def isPalindrome(self, s):
        for ch in string.punctuation:
            s=s.replace(ch,' ')
        arr=s.split()
        s=''.join(arr).lower()
        left=0
        right=len(s)-1
        while left<=right:
            if s[left]!=s[right]:
                return False
            left+=1
            right-=1
        return True
