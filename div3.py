# A
# t = int(input())
# while t > 0:
#     arr = list(map(int, input().split()))
#     brr = sorted(arr)
#     mx = 0
#     for i in range(5):
#         brr[0] += 1
#         brr = sorted(brr)
#     print(brr[0] * brr[1] * brr[2])
#     t -= 1
#
# import math
# t = int(input())
# arr = list(map(int, input().split()))
# x = int(2 * sum(arr)/len(arr))
# # print(x)
# srr = set()
# for i in range(t):
#     for j in range(t):
#         if arr[i] + arr[j] == x and (i not in srr and j not in srr) and (i != j):
#             print(f"{i+1} {j+1}")
#             srr.add(i)
#             srr.add(j)

# # practice recursion
#
# def print_x(n):
#     if n == 0:
#         return 1
#     else:
#         print(n)
#         print_x(n-1)
# print_x(7)
#
#
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#
#         return n * factorial(n - 1)
#
#
# x = factorial(6)
# print(x)
#
#
n, d = map(int, input().split())
count = 0
cnt = 0
counts = []
while d > 0:
    x = input()
    arr = [int(i) for i in x]
    # print(arr)
    if sum(arr) != n:
        count += 1
        counts.append(count)
#         print("hellow")
    else:
        count = 0
#         print(":asdlfj")
    d -= 1

try:
    print(max(counts))
except:
    print(count)
