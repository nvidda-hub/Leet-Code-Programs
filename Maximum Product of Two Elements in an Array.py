num_list = []
n = int(input("Enter number of elements:- "))
for i in range(n):
    print("Enter", i + 1, "th element :- ", end="")
    ele_input = int(input())
    num_list.append(ele_input)

print("list : ", num_list)


count = 0
max_value = 0
for i in range(n):
    for j in range(n):
        if i != j:
            max_value_new = (num_list[i] - 1)*(num_list[j] - 1)
            count = count + 1
        else:
            continue
        if max_value_new > max_value:
            max_value = max_value_new
        else:
            continue
print("maximum product in list : ", max_value)