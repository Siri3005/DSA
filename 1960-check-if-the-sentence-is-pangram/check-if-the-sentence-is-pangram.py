class Solution(object):
    def checkIfPangram(self, sentence):
        alpha=set('abcdefghijklmnopqrstuvwxyz')
        if set(sentence)==alpha:
            return True
        else:
            return False