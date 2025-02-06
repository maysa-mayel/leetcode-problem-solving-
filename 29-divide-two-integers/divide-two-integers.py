class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor!=0 :
            out = (abs(dividend) / abs(divisor))
            sign= -1 if (divisor < 0 and dividend >0) or (divisor >0 and dividend <0) else 1 
        res = sign*out
        if res> (2**31 - 1):
            res=2**31 - 1
        if res < (-(2**31)):
            res = -2**31
        return res 


        