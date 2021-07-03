candies_list = []
n = int(input("Enter number of students for candy:- "))
for i in range(n):
    print("Candies for student", i+1, "= ", end="")
    numberOfCandy = int(input())
    print(end="")
    candies_list.append(numberOfCandy)


print(candies_list)
maxNumber = candies_list[1]
for i in range(n-1):
    if candies_list[i+1] >= maxNumber:
        maxNumber = candies_list[i+1]

extra_candies = int(input("Enter extra number of candies = "))
boolean_list = []
for i in range(n):
    if candies_list[i] + extra_candies >= maxNumber:
        boolean_list.append("true")
    else:
        boolean_list.append("false")

print(boolean_list)