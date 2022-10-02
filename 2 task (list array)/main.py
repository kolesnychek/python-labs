lst = input().split()
for i in range(len(lst)):
    lst[i] = float(lst[i])
print(lst)

j = 1
for j in range(len(lst)-1):
    if lst[j-1] < lst[j] and lst[j] < lst[j+1]:
        print(j, " - index of right element (", lst[j],") in sequence ", lst[j-1], ", ", lst[j], ", ", lst[j+1])
