upper = ["A", 'B', 'C', 'D', 'E', 'F', 'G', 'H','I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lower = [i.lower() for i in upper]
# print(lower)
# print(len(upper))

n = int(input())
count = 0
while n > 0:
    arr = list(input().strip())
#     print(arr)
    for i in arr:
        if i == "P":
            count += 1
        if i == "p":
            count += 1

    n -= 1
print(count)
