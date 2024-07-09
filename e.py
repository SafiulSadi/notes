upper = ["A", 'B', 'C', 'D', 'E', 'F', 'G', 'H','I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
a = input()
b = input()
arr = [i for i in a]
brr = [i for i in b]
# arr = sorted(arr)
# brr = sorted(brr)
count = 0
for i in range(len(arr)):
    if arr[i] != brr[i]:
        count += 1
print(count)


t7 =0
z=12