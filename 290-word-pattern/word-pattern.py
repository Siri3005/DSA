class Solution(object):
    def wordPattern(self, pattern, s):
        hashmap={}
        arr=s.split()
        visited=set()
        if len(pattern)!=len(arr):
            return False
        for i in range(len(pattern)):
            if pattern[i] in hashmap:
                if hashmap[pattern[i]]!=arr[i]:
                    return False
            else:
                if arr[i] in visited:
                    return False
                hashmap[pattern[i]]=arr[i]
                visited.add(arr[i])
        return True