class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        hammingdistance = 0 
        calx= x
        caly = y
        while calx !=0 or caly !=0:
            bitx = calx %2
            bity = caly %2
            if bitx!=bity:
                hammingdistance =hammingdistance+1
            calx = calx//2
            caly = caly//2
        return hammingdistance


            

        



if __name__=="__main__":
    sl = Solution()
    x=1
    y=4
    print(sl.hammingDistance(x,y))