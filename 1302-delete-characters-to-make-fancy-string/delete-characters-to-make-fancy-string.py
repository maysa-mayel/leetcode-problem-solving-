class Solution:
    def makeFancyString(self, s: str) -> str:
        count=0
        char=''
        l=list()
        for i in s:
            if char==i: 
                count+=1
            else:
                char=i
                count=1
            if count<3:
                l.append(char)
        return "".join(l)
            
            
        