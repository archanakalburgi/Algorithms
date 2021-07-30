'''
[1, 2, 3] -> [1,2,4]
[1, 0, 9, 9] -> [1, 1, 0, 0]
[9,9] -> [1, 0, 0]
'''

def convert_roman(string):
    Roman_number = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    integer = 0 
    for i in range(len(string)-1):
        romanChar = string[i]
        romanNum = string[i+1]

        if Roman_number[romanChar] < Roman_number[romanNum]:
            integer -= Roman_number[romanChar]
        else:
            integer += Roman_number[romanChar]
    
    integer += Roman_number[string[-1]]

    return integer

print(convert_roman("XVI")) 