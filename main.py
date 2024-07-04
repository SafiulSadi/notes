# # Write a program to reverse a string.
#
# x = input()
# arr = []
# for i in x:
#     arr.append(i)
# # arr.reverse()
# start = 0
# end = len(arr) - 1
# while start < end:
#     temp = arr[start]
#     arr[start] = arr[end]
#     print(arr[start])
#     arr[end] = temp
#     start += 1
#     end -= 1
# print(arr)
# a = ""
# for i in arr:
#     a += i
# print(a)
#
# 55 A. Mishka and Game

n = int(input())
mik = 0
chris = 0
while n > 0:
    m, c = map(int, input().split())
    if c > m:
        chris += 1
    elif m > c:
        mik +=1
    n -= 1

if mik > chris:
    print("Mishka")
elif chris > mik:
    print("Chris")
else:
    print("Friendship is magic!^^")

