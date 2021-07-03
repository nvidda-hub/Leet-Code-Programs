num_list = []
index_list = []
n = int(input("Number of element in both list :- "))

for i in range(n):  # number list
    print("Number", i+1, "th list elements :- ", end="")
    numElement = int(input())
    num_list.append(numElement)


for i in range(n):  # index list
    print("Index", i+1, "th list elements :- ", end="")
    indexElement = int(input())
    print(end="")
    index_list.append(indexElement)

print("number list :- ", num_list)
print("index list :- ", index_list)

target_array = []
for i in range(n):
    target_array.insert(index_list[i], num_list[i])

print("Target array :- ", target_array)