import string
widths = [10, 10, 10, 10, 10, 10, 10, 10, 10,
          10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]

user_choice = input("Enter YES to change value at index or NO :- ").lower()

if user_choice == 'yes':
    number_of_index = int(input("Enter number of index have to changed :- "))
    for i in range(number_of_index):
        n = int(input("Enter index to change number of units: "))
        value = int(input("Enter the width from 2 to 10 :- "))
        widths[n] = value
elif user_choice == 'no':
    print(widths)

# storing into a dictionary with a to z chars
charDict = {}
for i in range(26):
    charDict[string.ascii_lowercase[i]] = widths[i]

letter_str = input("Enter string :- ")

output = []
line_counter = 1
width_counter = 0
remain_width = 0
cum_sum = []
for i in range(letter_str.__len__()):
    width_counter = width_counter + charDict[letter_str[i]]
    cum_sum.append(width_counter)
    if width_counter <= 100:
        remain_width = 100 - cum_sum[i]
    elif cum_sum[i] > 100:
        remain_width = remain_width + cum_sum[i] - 100
        line_counter = line_counter + 1
        width_counter = 0

print(cum_sum)
output.append(line_counter)
output.append(remain_width)
print("Output :", output)
