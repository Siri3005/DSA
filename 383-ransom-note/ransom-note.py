class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        if len(ransomNote)>len(magazine):
            return False
        magazine=list(magazine)
        for i in range(len(ransomNote)):
            if ransomNote[i] not in magazine:
                return False
            idx=magazine.index(ransomNote[i])
            del magazine[idx]
        return True
        