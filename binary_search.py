def search_binary(nums, target_number):
    for index, value in enumerate(nums, start=0):
        if value == target_number:
            return index
        else:
            continue
    return -1


def input_lst(ls_size):
    ls = []
    for i in range(ls_size):
        print("element ", i+1, end=" = ")
        element = int(input())
        ls.append(element)
    return ls


n = int(input("Enter size of list: "))
target_value = int(input("Enter target value : "))
list1 = input_lst(n)
print("INPUT : ", list1)
print("OUTPUT : ", search_binary(list1, target_value))
