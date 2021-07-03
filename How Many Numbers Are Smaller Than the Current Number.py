num_list = []
n = int(input("Enter number of in list :- "))
for i in range(n):
    element = int(input())
    num_list.append(element)
print("Number list :- ", num_list)

count_list = []
count = 0
for i in range(n):
    for j in range(n):
        if num_list[j] < num_list[i] and i != j:
            count = count + 1

    count_list.append(count)
    count = 0

print(count_list)