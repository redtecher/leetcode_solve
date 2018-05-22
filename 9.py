class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        if x<0:
            return False
        elif x==0:
            return True
        else:
            
            
            lst=[]
            while x!=0 :
                getnum=x%10
                x=x//10
                lst.append(getnum)

            
            length = len(lst)
            
            flag = 1
            
            for i in range(length//2+1):
                
                if lst[i]==lst[-i-1]:
                    continue
                else:
                    flag=0
                    break
                

            if flag==1:
                return True
            else :
                return False

        




if __name__ == '__main__':
    sl =Solution()
    print(sl.isPalindrome(1))