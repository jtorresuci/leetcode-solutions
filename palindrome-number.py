# Given an integer x, 
# return true if x is palindrome integer.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]