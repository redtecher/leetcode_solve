class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        getlist = []
        for i in range(left,right+1):
            newi = i
            flag =0
            while newi!=0:
                getbit = newi % 10
                if getbit==0:
                    flag =1
                    break
                if i %getbit !=0:
                    flag =1
                newi = newi //10
            if flag == 0:
                getlist.append(i)
            
        
        return getlist
                


if __name__=='__main__':
    sl =Solution()
    sl.selfDividingNumbers(1,22)



