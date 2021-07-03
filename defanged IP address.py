print("Enter a valid IP v4 address 'x.x.x.x' format :- ")
IP_address = str(input())
count = 0
flag = 0
defanged_IP_address = []
for i in range(len(IP_address)):
    if IP_address[i] != ".":
        flag = flag +  1
        continue
    elif flag <= 3 and IP_address[i] == "." :
            count = count + 1
            defanged_IP_address = IP_address.replace(".","[.]")
            flag = 0
if count == 3:
    print(defanged_IP_address)
else:
    print("Please enter a valid IPv4 address.")

