class Solution(object):
    def numIslands(self, grid):
        if not grid:
            return 0
        rows=len(grid)
        cols=len(grid[0])
        visited=set()
        num_islands=0
        def bfs(r,c):
            queue=collections.deque()
            visited.add((r,c))
            queue.append((r,c))
            while queue:
                row,col=queue.popleft()
                dirn=[[0,1],[1,0],[-1,0],[0,-1]]
                for dr,dc in dirn:
                    urow,ucol=row+dr,col+dc
                    if urow in range(rows) and ucol in range(cols) and (urow,ucol) not in visited and grid[urow][ucol]=='1':
                        queue.append((urow,ucol))
                        visited.add((urow,ucol))
        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visited and grid[r][c]=='1':
                    bfs(r,c)
                    num_islands+=1
        return num_islands
        