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
# # 55 A. Mishka and Game
#
# n = int(input())
# mik = 0
# chris = 0
# while n > 0:
#     m, c = map(int, input().split())
#     if c > m:
#         chris += 1
#     elif m > c:
#         mik +=1
#     n -= 1
#
# if mik > chris:
#     print("Mishka")
# elif chris > mik:
#     print("Chris")
# else:
#     print("Friendship is magic!^^")
#

"""
algo expert problems for the coding test.
"""
#
# # O(n^2) time | o(1) space
# def two_number_sum(array, target_sum):
#     for i in range(len(array) - 1):
#         first_num = array[i]
#         for j in range(i + 1, len(array)):
#             second_num = array[j]
#             if first_num + second_num == target_sum:
#                 return[first_num, second_num]
#     return []


# # O(n) time | O(n) space
# def two_number_sum(array, target_sum):
#     nums = {}
#     for num in array:
#         if target_sum - num in nums:
#             return [target_sum - num, num]
#         else:
#             nums[num] = True
#     return []
#
# def two_number_sum(array, target_sum):
#     array.sort()
#     left = 0
#     right = len(array) - 1
#     while left < right:
#         current_sum = array[left] + array[right]
#         if current_sum == target_sum:
#             return [array[left], array[right]]
#         elif current_sum < target_sum:
#             left += 1
#         elif current_sum > target_sum:
#             right -= 1
import math
import sys

# arr = []
odd = 0
even = 0
input = sys.stdin.read
arr = data = sys.stdin.read().strip().split('\n')

# for i in data:
#     try:
#         a = input()
#     except EOFError:
#         break
#     else:
#         arr.append(a)
#         print(arr)
# print(arr)
max_len = 0
for i in arr:
    if len(i) > max_len:
        max_len = len(i)
        # print("hlo")

    else:
        pass
#         print("hi")
print("*" * (max_len + 2))
for i in arr:
    if len(i) <= max_len:
        if (max_len % 2 == 0 and len(i) % 2 == 0) or (max_len % 2 == 1 and len(i) % 2 == 1):
            g = math.floor((max_len - len(i))/2)
            space = " " * (g)
            i = "*" + space + i + space + "*"
            print(i)
        elif max_len % 2 == 0 and len(i) % 2 == 1:
            g = math.ceil((max_len - len(i)) / 2)
            space = " " * (g)
            if odd % 2 == 0:
                odd += 1
                i = "*" + " " * (g - 1) + i + space + "*"
                print(i)
            if odd % 2 == 1:
                odd += 1
                i = "*" + space + i + " " * (g - 1) + "*"
        elif max_len % 2 == 1 and len(i) % 2 == 0:
            g = math.floor((max_len - len(i)) / 2)
            space = " " * (g)
            if even % 2 == 0:
                even += 1
                i = "*" + " " * (g - 1) + i + space + "*"
                print(i)
            if even % 2 == 1:
                even += 1
                i = "*" + space + i + " " * (g - 1) + "*"
                print(i)

print("*" * (max_len + 2))

# print(arr)
# print("*" * (max_len + 2))
