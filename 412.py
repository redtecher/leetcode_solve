#一次通过
class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        for i in range(n):
            print(i+1)
            if (i+1)%3==0 and (i+1)%5==0:
                result.append("FizzBuzz")
                continue
            if (i+1)%3==0:
                result.append('Fizz')
                continue
            if (i+1)%5==0:
                result.append('Buzz')
                continue
            result.append(str(i+1))
        return(result)
            
                
                

        

if __name__=='__main__':
    sl = Solution()
    print(sl.fizzBuzz(15))