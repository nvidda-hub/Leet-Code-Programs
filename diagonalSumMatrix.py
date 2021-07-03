ls = []
n = int(input("Enter order of square matrix :- "))
for i in range(n):
    ls1 = []
    for j in range(n):
        print("A", i+1, j+1, end=" = ")
        e = int(input())
        ls1.append(e)
    ls.append(ls1)

print(ls)
diaSum = 0
avg = int((n+1)/2)

for i in range(n):
    for j in range(n):
        if i == j:
            diaSum = diaSum + ls[i][j]
        elif (i + j) == (n-1):
            diaSum = diaSum + ls[i][j]
        else:
            continue

print(diaSum)
