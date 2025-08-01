class Solution(object):
    def deleteGreatestValue(self, grid):
        res=0
        while len(grid[0])!=0:
            max_r=0
            for row in grid:
                max_r=max(max_r,max(row))
                row.remove(max(row))
            res+=max_r
        return res
        