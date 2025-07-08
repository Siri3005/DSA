class Solution(object):
    def merge(self, intervals):
        intervals.sort(key=lambda i:i[0])
        currInterval=intervals[0]
        res=[]
        for i in range(1,len(intervals)):
            if currInterval[1]<intervals[i][0]:
                res.append(currInterval)
                currInterval=intervals[i]
            elif intervals[i][0]<=currInterval[1]:
                currInterval=[min(currInterval[0],intervals[i][0]),max(currInterval[1],intervals[i][1])]
        res.append(currInterval)
        return res
            