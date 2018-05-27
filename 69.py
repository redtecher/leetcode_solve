#开始觉得这题贼简单，后来发现其实没那么简单，，果然超时了，然后想 ，用二分查找解决

class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """

        if x==1 :
            return 1
        start = 0
        end = x//2+1

        while end-start>1:
            #print(start,end)
            if ((start+end)//2)**2==x:
                return (start+end)//2
            elif ((start+end)//2)**2>x:
                end=(start+end)//2
            else:
                start=(start+end)//2
        
        return start
            
            
        
        
            
            





if __name__=='__main__':
    sl=Solution()
    print(sl.mySqrt(4))