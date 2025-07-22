class Solution(object):
    def findReplaceString(self, s, indices, sources, targets):
        s_list=list(s)
        for i in range(len(indices)):
            idx=indices[i]
            target=targets[i]
            src=sources[i]
            if s[idx:idx+len(src)]==src:
                s_list[idx]=target
                for j in range(idx+1,idx+len(src)):
                    s_list[j]=''
            
        return ''.join(s_list)