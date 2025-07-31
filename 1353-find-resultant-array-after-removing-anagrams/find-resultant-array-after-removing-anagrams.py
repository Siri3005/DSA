class Solution(object):
    def removeAnagrams(self, words):
        result=[words[0]]
        for i in range(1,len(words)):
            if sorted(result[-1])!=sorted(words[i]):
                result.append(words[i])
        return result
                