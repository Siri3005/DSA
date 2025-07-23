class Solution(object):
    def findKthBit(self, n, k):
        def invert(string):
            string=list(string)
            for i in range(len(string)):
                if string[i]=='0':
                    string[i]='1'
                elif string[i]=='1':
                    string[i]='0'
            return ''.join(string)
        s=['']*(n+1)
        s[1]='0'
        for i in range(2,n+1):
            s[i]=s[i-1]+"1"+invert(s[i-1])[::-1]
        return s[n][k-1]