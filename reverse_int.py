# Given a 32-bit signed integer, reverse digits of an integer.

# Example: Input: 123, Output: 321

# Example: Input: -123, Output: -321

# Example: Input: 120, Output: 21


#!/usr/bin/env python3
class Solution:
    def reverse(self, x: int) -> int:
        if x>=0:
            x=int(str(x)[::-1])
        else:
            x=-int(str(-x)[::-1])
        return x if x<=(2**31-1) and x>=-(2**31) else 0
