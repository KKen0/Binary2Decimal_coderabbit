rawNum = input("Enter 8 digit binary digits: ")

total = 0

if len(rawNum) <= 8:
    for char in rawNum:
        if char == '1' or char == '0':
            total = total * 2 + int(char)
        else:
            raise ValueError("Invalid binary number")
    print(total)
else:
    print("Binary digits should be lower than or equal to 8 digits")
