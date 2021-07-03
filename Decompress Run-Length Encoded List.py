            # Decompress Run-Length Encoded List
num_list = []
n = int(input("Enter number elements in list :- "))
for i in range(n):
    element = int(input())
    num_list.append(element)
print("number list :- ", num_list)
decompress_list = []
if n % 2 == 0:
    for i in range(0, n-1, 2):
        freq = num_list[i]
        val = num_list[i+1]
        for k in range(freq):
            decompress_list.append(val)
else:
    print("Please enter even number of elements")
print(decompress_list)