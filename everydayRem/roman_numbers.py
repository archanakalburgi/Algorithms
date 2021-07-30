
def romanNumbers(roman_string):
    Roman_number = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    
    integer = 0
    for i in range(len(roman_string) - 1):
        roman_char = roman_string[i]
        roman_num = roman_string[i + 1]
        if Roman_number[roman_char] < Roman_number[roman_num]:
            integer -= Roman_number[roman_char]
        
        else:
            integer += Roman_number[roman_char]
    integer += Roman_number[roman_string[-1]]
    return integer 

print(romanNumbers("XI"))