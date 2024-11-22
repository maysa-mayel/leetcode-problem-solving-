class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Handle the case where n is negative
        if n < 0:
            x = 1 / x  # Invert the base for negative exponents
            n = abs(n) # Make the exponent positive
        
        result = 1
        while n > 0:
            if n % 2 == 1:  # If n is odd, multiply by the base
                result *= x
            x *= x  # Square the base for the next iteration
            n //= 2  # Divide the exponent by 2
        
        return result