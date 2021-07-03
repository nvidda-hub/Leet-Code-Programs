def match_prefix_suffix(ls1, ls2):
    match_str = "none"
    max_length = 0
    for k in range(len(ls1)):
        if ls1[k] == ls2[k] and max_length < len(ls1[k]):
            max_length = len(ls1[k])
            match_str = ls1[k]
        else:
            continue
    return match_str


str_input = input("Enter string : ")
prefix_list = []
suffix_list = []

val_prefix = ""
val_suffix = ""

# for suffix
for i in range(len(str_input)-1):
    val_prefix = val_prefix + str_input[i]
    prefix_list.append(val_prefix)

# for prefix
i = len(str_input)-1
while i > 0:
    val_suffix = str_input[i] + val_suffix
    suffix_list.append(val_suffix)
    i = i - 1

print("Prefix list : ", prefix_list)
print("Suffix list : ", suffix_list)

print(match_prefix_suffix(prefix_list, suffix_list))


