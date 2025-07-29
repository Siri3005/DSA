class Solution(object):
    def maxDistance(self, colors):
        max_d=0
        for i in range(len(colors)):
            for j in range(len(colors)):
                if i!=j:
                    if colors[i]!=colors[j]:
                        max_d=max(max_d,abs(j-i))
        return max_d