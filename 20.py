#堆栈，不多说了 类似计算器的实现


class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        searchfor = {
            '(':'1',
            '[':'2',
            '{':'3',
            '}':'{',
            ']':'[',
            ')':'('

        }

        length = len(s)
        list = []
        for i in range(length):
            if len(list)==0:
                list.append(s[i])
                
                continue
            up=s[i]
            down =list.pop()
            
            if searchfor[up]==down:
                continue
            else:
                list.append(down)
                list.append(up)
            
        


            
            
        if list == []:
            
            return True
        else:
            return False

        


if __name__ =="__main__":
    sl =Solution()
    print(sl.isValid("()[]{}"))

