class Solution(object):
    def sortSentence(self, s):
        arr=s.split()
        res=['']*len(arr)
        for word in arr:
            curr=list(word)
            res[int(curr[-1])-1]=''.join(curr[:-1])
        return ' '.join(res)
        