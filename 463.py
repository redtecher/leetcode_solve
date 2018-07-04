class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        lengthy = len(grid)
        lengthx =len(grid[0])
        
        result = 0
        for i in range(lengthx):
            for j in range(lengthy):
                if grid[j][i]==1:
                    if i-1<0 or grid[j][i-1] ==0:
                        result=result+1
                    if j-1<0 or grid[j-1][i]==0:
                        result=result+1

                    if i+1>=lengthx or grid[j][i+1]==0:
                        result=result+1
                    if j+1 >=lengthy or grid[j+1][i]==0:
                        result=result+1
                else:
                    continue
            
        return result
                    
                

    
               



if __name__=='__main__':
    sl=Solution()
    grid=[[1,0]]
    
    print(sl.islandPerimeter(grid))