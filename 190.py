#列表化，然后颠倒，再次计算。应该还能算法优化，有时间再想。。
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        lst = []
        while n!=0:
            lst.append(n%2)
            n=n//2
        
        length=len(lst)
        for i in range(32-length):
            lst.append(0)
        lst.reverse()
        result = 0
        

        for i in range(32):
            
            result=result+lst[i]*(2**i)
        return result
        





if __name__=="__main__":
    sl = Solution()
    sl.reverseBits(43261596)