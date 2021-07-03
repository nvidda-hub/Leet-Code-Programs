head_list = []
n = int(input("Enter number of elements in head list 0 or 1:- "))
binary_to_integer = 0
count = 0
error_element = []
for i in range(n, 0, -1):
    print("Enter", n - i + 1, "th binary input :- ", end="")
    binary_input = int(input())
    if binary_input == 0 or binary_input == 1:
        head_list.append(binary_input)
        binary_to_integer = binary_to_integer + binary_input * (2 ** (i - 1))
        count = count + 1
    else:
        error_element.append(n - i + 1)


if count == n:
    print("head :- ", head_list)
    print("Integer from binary input : ", binary_to_integer)
else:
    print("Try to enter binary element 0 or 1 or check these elements ", error_element)
