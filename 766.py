class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        lengthx= len(matrix[0])
        lengthy= len(matrix)
        for k in range(lengthy):
            for i in range(lengthx):
                for j in range(lengthx):
                    matrix[i][j]


                


if __name__=="__main__":
    sl = Solution()
    matrix = [
    [1,2,3,4],
    [5,1,2,3],
    [9,5,1,2]
    ]
    sl.isToeplitzMatrix(matrix)