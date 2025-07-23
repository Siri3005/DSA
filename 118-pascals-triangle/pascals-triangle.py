class Solution(object):
    def generate(self, numRows):
        arr=[1]
        res=[]
        res.append(arr)
        prev_arr=arr
        for i in range(1,numRows):
            new_arr=[]
            for j in range(i+1):
                if j==0 or j==i:
                    new_arr.append(1)
                else:
                    new_arr.append(prev_arr[j-1]+prev_arr[j])
            res.append(new_arr)
            prev_arr=new_arr
        return res

        