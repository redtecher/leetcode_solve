class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        result = 0
        flag = -1
        while num!=0:
            getbit = num %2 
            flag = flag+1
            num = num//2
            if getbit == 0:
                result = (2**flag)+result

        return result
                
                
        

if __name__=='__main__':
    sl = Solution()
    print(sl.findComplement(5))