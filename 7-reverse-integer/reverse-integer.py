class Solution:
    def reverse(self, x: int) -> int:
      sign = -1 if x < 0 else 1
      s=str(abs(x))[::-1]
      out=int(s)*sign
      if not(-(2**31)<=out<=(2**31)-1):
         return 0
      return out 