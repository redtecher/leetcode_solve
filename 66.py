#把这道题当模拟题在做。。。。应该有倒序加法解决 。。。以前用C能写，Python再想想吧。。

class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        length = len(digits)
        result = 0
        for i in range(length):
            
            result =result+digits[i]*(10**(length-i-1))
        result = result+1
        rehaha=[]
        while result != 0 :
            newnum = result%10
            rehaha.append(newnum)
            result=result//10
        rehaha.reverse()


        return rehaha
            
        
        




if __name__=='__main__':
    sl=Solution()
    print(sl.plusOne([9,9,9,9]))