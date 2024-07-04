# Write a program to reverse a string.

x = input()
arr = []
for i in x:
    arr.append(i)
# arr.reverse()
start = 0
end = len(arr) - 1
while start < end:
    temp = arr[start]
    arr[start] = arr[end]
    print(arr[start])
    arr[end] = temp
    start += 1
    end -= 1
print(arr)
a = ""
for i in arr:
    a += i
print(a)

