class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dic = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        sum = 0
        for i in range(len(s)):
            sum += roman_dic[s[i]]
            if i != len(s) - 1 and roman_dic[s[i]] < roman_dic[s[i + 1]]:
                sum = sum - roman_dic[s[i]] - roman_dic[s[i]]
        return sum