start_time_list = []
end_time_list = []

n = int(input("Enter number of students:- "))

for i in range(n):
    element_start = int(input())
    start_time_list.append(element_start)
print("Start time : ", start_time_list)

for i in range(n):
    element_end = int(input())
    end_time_list.append(element_end)
print("End time : ", end_time_list)

query_time = int(input("Enter Query time : "))

count = 0

for i in range(n):
    if start_time_list[i] <= query_time <= end_time_list[i]:
        count = count + 1
    else:
        continue

print("Number of students done homework in query time : ", count)