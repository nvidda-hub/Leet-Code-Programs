digit = input("Enter number formed by 9 and 6 only :- ")
max_number = int(digit)
i = 0
while i < len(digit):
    temp = digit[i]
    if temp == "9":
        temp = "6"
        str_digit = digit[:i] + temp + digit[i+1:len(digit)]
        if int(str_digit) <= max_number:
            i = i + 1
        else:
            max_number = int(str_digit)
            i = i + 1
    elif temp == "6":
        temp = "9"
        str_digit = digit[:i] + temp + digit[i+1:len(digit)]
        if int(str_digit) <= max_number:
            i = i + 1
        else:
            max_number = int(str_digit)
            i = i + 1
    else:
        print("Error --> Number other than 9 and 6 found, check", i+1, "th place.")
        break
print(max_number)