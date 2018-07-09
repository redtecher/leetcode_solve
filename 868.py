class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """

        lengthy  = len(A)
        lengthx = len(A[0])
        result=[]
        for i in range(lengthx):
            newone = []
            for j in range(lengthy):
                newone.append(A[j][i])
            result.append(newone)

        return result
        


if __name__=="__main__":
    sl = Solution()
    A=[[1,2,3],[4,5,6]]
    print(sl.transpose(A))