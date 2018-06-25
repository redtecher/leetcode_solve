class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        length = len(A)
        for i in range(length):
            A[i].reverse()
            #print(A)
            lengthy = len(A[i])
            for j in range(lengthy):
                if A[i][j]==1 :
                    A[i][j]=0
                    #print(i,j,A[i][j])
                    continue
                if A[i][j]==0 :
                    A[i][j]=1
                    #print(i,j,A[i][j])
                    continue
        return A
        


if __name__=='__main__':
    sl = Solution()
    A=[[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
    print(sl.flipAndInvertImage(A))