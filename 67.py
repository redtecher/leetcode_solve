#纯模拟，感觉好像做复杂了。。。


class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if a=='0' and b=='0':
            return "0"
        list_a =list(a)
        list_b = list(b)
        list_a.reverse()
        list_b.reverse()
        length_a = len(list_a)
        length_b = len(list_b)
        if length_a>=length_b:
            length = length_a
            for i in range(length_a-length_b):
                list_b.append('0')
        else:
            length = length_b
            for i in range(length_b-length_a):
                list_a.append('0')
        #print(a,list_a)
        #print(b,list_b)
        
        
        result = []
        plus = 0 
        for i in range(length):
            
            if ord(list_a[i])+ord(list_b[i])-2*ord('0')+plus>=2:
                #print(ord(list_a[i])-ord('0'),ord(list_b[i])-ord('0'),ord(list_a[i])+ord(list_b[i])-2*ord('0')+plus-2)
                
                result.append(ord(list_a[i])+ord(list_b[i])-2*ord('0')+plus-2)    
                plus=1     
                #print(result)
            else:
                #print(ord(list_a[i])-ord('0'),ord(list_b[i])-ord('0'),ord(list_a[i])+ord(list_b[i])-2*ord('0')+plus)
               
                result.append(ord(list_a[i])+ord(list_b[i])-2*ord('0')+plus)

                plus=0
                #print(result)
        if plus==1:
            result.append(1)
        print(result)
        result.reverse()
        
        count=0
        for i in result:
            if i==0:
                count = count+1
            else:
                break
        #print(count)
        result=result[count:]
        newresult = []
        for i in result:
            newresult.append(chr(i+ord('0')))
        
                
            
                
        return "".join(newresult)
                
        




if __name__=='__main__':
    sl=Solution()
    print(sl.addBinary('0','0'))