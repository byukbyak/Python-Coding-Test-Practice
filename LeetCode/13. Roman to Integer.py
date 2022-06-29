class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {
            'I' : 1,
            'IV': 4,
            'V' : 5,
            'VI': 6,
            'IX': 9,
            'X' : 10,
            'XI': 11,
            'XL': 40,
            'L' : 50,
            'LX': 60,
            'XC': 90,
            'C' : 100,
            'CX': 110,
            'CD': 400,
            'D' : 500,
            'DC': 600,
            'CM': 900,
            'M' : 1000
        }
        print(roman_dict)
        
        result = 0
        cursor = 0
        
        while cursor < len(s):
            if (cursor+1) != len(s):
                if s[cursor]+s[cursor+1] in roman_dict:
                    result += roman_dict[s[cursor]+s[cursor+1]]
                    cursor += 2
            else: # cursor == len(s)]
                result += roman_dict[s[cursor]]
                cursor += 1
        
        return result