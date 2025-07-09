class Solution(object):
    def spiralOrder(self, matrix):
        res=[]
        l=0
        r=len(matrix[0])-1
        top=0
        bottom=len(matrix)-1
        while l<=r and top<=bottom:
            for i in range(l,r+1):
                res.append(matrix[top][i])
            top+=1
            for j in range(top,bottom+1):
                res.append(matrix[j][r])
            r-=1
            if top<=bottom:
                for k in range(r,l-1,-1):
                    res.append(matrix[bottom][k])
                bottom-=1
            if l<=r:
                for t in range(bottom,top-1,-1):
                    res.append(matrix[t][l])
                l+=1
        return res