class Solution(object):
    def generate(self, numRows):
        first_row=[1]
        res=[]
        res.append(first_row)
        pre_row=first_row
        for i in range(1,numRows):
            curr_row=[1]*(i+1)
            for j in range(i+1):
                if j==0 or j==i:
                    continue
                else:
                    curr_row[j]=pre_row[j]+pre_row[j-1]
            res.append(curr_row)
            pre_row=curr_row
        return res



        