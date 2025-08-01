class Solution(object):
    def mergeSimilarItems(self, items1, items2):
        res=[]
        hashmap={}
        notv=[]
        visited=[]
        for item in items2:
            hashmap[item[0]]=item[1]
        for item in items1:
            if item[0] in hashmap:
                res.append([item[0],item[1]+hashmap[item[0]]])
                visited.append(item[0])
            else:
                notv.append(item)
        for item in items2:
            if item[0] not in visited:
                res.append(item)
        res=res+notv
        res.sort(key=lambda x:x[0])
        return res

        