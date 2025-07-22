class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        '''hashmap={}
        
        for ch in string.punctuation:
            paragraph=paragraph.replace(ch,' ')
        arr=paragraph.lower().split()
        for word in arr:
            if word not in banned:
                hashmap[word]=hashmap.get(word,0)+1
        maxm=0
        res=''
        for key,val in hashmap.items():
            if val>maxm:
                maxm=val
                res=key
        return res'''
        hashmap={}
        for ch in string.punctuation:
            paragraph=paragraph.replace(ch,' ')
        arr=paragraph.lower().split()
        for word in arr:
            if word not in banned:
                hashmap[word]=hashmap.get(word,0)+1
        maxm=0
        res=''
        for key,val in hashmap.items():
            if val>maxm:
                maxm=val
                res=key
        return res
