"""
342. Power of Four
Easy

Given an integer n, return true if it is a power of four. Otherwise, return false.

An integer n is a power of four, if there exists an integer x such that n == 4x.



Example 1:

Input: n = 16
Output: true
Example 2:

Input: n = 5
Output: false
Example 3:

Input: n = 1
Output: true


Constraints:

-231 <= n <= 231 - 1


Solution:

constraints: if n == 0, False
if n < 0, False -> negative log not possible
the log is the inverse of the exponential
n == 4^x
log(n) = log(4)^x
log(n) = x log(4)
log(n)/log(4) = x

O(1): runtime
o(1): space complexity

"""

import math
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 0:
            return False
        if n < 0:
            return False
        x = math.log(n)/math.log(4)
        if x.is_integer():
            return True
        else:
            return False
