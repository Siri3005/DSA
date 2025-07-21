class Solution(object):
    def findWords(self, words):
        first=set('qwertyuiop')
        second=set('asdfghjkl')
        third=set('zxcvbnm')
        res=[]
        for word in words:
            lower_word_set = set(word.lower()) 
            if lower_word_set.issubset(first) or lower_word_set.issubset(second) or lower_word_set.issubset(third):
                res.append(word)
        return res
        
            
        
