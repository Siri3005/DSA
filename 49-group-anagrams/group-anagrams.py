class Solution(object):
    def groupAnagrams(self, strs):
        res=[]
        visited=set()
        sorted_strs = [''.join(sorted(s)) for s in strs]
        for i in range(len(strs)):
            if i in visited:
                continue
            list1=[strs[i]]
            for j in range(i+1,len(strs)):
                if j not in visited and sorted_strs[i]==sorted_strs[j]:
                    list1.append(strs[j])
                    visited.add(j)
            res.append(list1)
            visited.add(i)
        return res
        