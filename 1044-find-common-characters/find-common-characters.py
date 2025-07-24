class Solution(object):
    def commonChars(self, words):
        res=[]
        for c in set(words[0]):
            min_count=words[0].count(c)
            for word in words[1:]:
                min_count=min(min_count,word.count(c))
            res.extend([c]*min_count)
        return res