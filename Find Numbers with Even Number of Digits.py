num_list = []
n = int(input("Number of element in both list :- "))

for i in range(n):  # number list
    print("Number", i+1, "th list elements :- ", end="")
    numElement = int(input())

    num_list.append(numElement)

print("number list :- ", num_list)


count= 0
for i in range(n):
    l = len(str(num_list[i]))
    if l % 2 == 0:
        count = count + 1
    else:
        continue
print("Numbers with even digits in list :- ", count)