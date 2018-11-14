class Solution(object):
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        # """
        
        bottomcontent = 0
        for i in grid:
            for j in i:
                if j!=0:
                    bottomcontent=bottomcontent+1

        leftcontent=0
        for i in grid:
            leftcontent = leftcontent+max(i)
        
        rightcontent=0
        rc=[]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i==0:
                    rc=grid[0]
                    continue
                else:
                    if grid[i][j]>rc[j]:
                        rc[j]=grid[i][j]
        for s in rc:
            rightcontent = rightcontent+s
        return rightcontent+leftcontent+bottomcontent






if __name__=='__main__':
    sl=Solution()
    print(sl.projectionArea([[1,1,1],[1,0,1],[1,1,1]]))