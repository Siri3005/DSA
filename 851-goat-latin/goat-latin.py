class Solution(object):
    def toGoatLatin(self, sentence):
        vowels=('a','e','i','o','u','A','E','I','O','U')
        sentence=sentence.split()
        res=[]
        i=1
        for word in sentence:
            if word[0] in vowels:
                new_word=word+'ma'+'a'*i
            else:
                new_word=word[1:]+word[0]+'ma'+'a'*i
            res.append(new_word)    
            i+=1
        return ' '.join(res)

        