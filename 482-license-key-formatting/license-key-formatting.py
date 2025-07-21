class Solution(object):
    def licenseKeyFormatting(self, s, k):
        s=s.replace('-','').upper()
        res=''
        first_group_len=len(s)%k or k
        res+=s[:first_group_len]
        for i in range(first_group_len,len(s),k):
            res+='-'+s[i:i+k]

        return res