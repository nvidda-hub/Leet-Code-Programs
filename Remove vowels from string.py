str_input = str(input("Enter a string :- "))
v_list = ["a", "e", "i", "o", "u"]
count = 0
str_input_m = []
for i in range(len(str_input)):
    if str_input[i] in v_list:
        count = count + 1
    else:
        str_input_m = str_input[i]
        print(str_input_m, end="")


print("\nNumber of vowels in", str_input, " = ", count)