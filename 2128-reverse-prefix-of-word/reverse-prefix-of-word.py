class Solution(object):
    def reversePrefix(self, word, ch):
        stack=[]
        found=False
        for i in range(len(word)):
            stack.append(word[i])
            if word[i]==ch:
                found=True
                break
        if not found:
            return word
        stack.reverse()
        res=''.join(stack)+word[i+1:]
        return res   
        