class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        rowbegin=0
        columnbegin=0
        rowend=n-1
        columnend=n-1
        result = [[0 for i in range(n)] for j in range(n)]
        mov_num=1
        while mov_num<=n*n:
            
            for y in range(columnbegin,columnend+1):
                result[rowbegin][y]=mov_num
                # print(mov_num)
                mov_num=mov_num+1
            rowbegin=rowbegin+1

            for x in range(rowbegin,rowend+1):
                result[x][columnend]=mov_num
                # print(mov_num)
                mov_num=mov_num+1
            columnend=columnend-1

            for y in range(columnend,columnbegin-1,-1):
                result[rowend][y]=mov_num
                # print(mov_num)
                mov_num=mov_num+1
            rowend=rowend-1

            for x in range(rowend,rowbegin-1,-1):
                result[x][columnbegin]=mov_num
                # print(mov_num)
                mov_num=mov_num+1
            columnbegin=columnbegin+1

            # print(rowbegin,rowend,columnbegin,columnend)

        
        return result

        
                
        


if __name__=='__main__':
    sl= Solution()
    print(sl.generateMatrix(3))
    