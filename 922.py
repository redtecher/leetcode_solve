class Solution:
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        oddnum=[]
        evennum=[]
        length = len(A)
        for number in A:
            if number%2==0:
                evennum.append(number)
            else:
                oddnum.append(number)
        result=[]
        for i in range(length):
            if i%2==0:
                result.append(evennum[i//2])
            else:
                result.append(oddnum[(i-1)//2])
        return result


if __name__=='__main__':
    sl = Solution()
    sl.sortArrayByParityII([4,2,5,7])