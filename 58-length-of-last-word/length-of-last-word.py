class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        strs=s.split()
        word=strs[-1]
        return len(word)