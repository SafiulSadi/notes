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


# 3Sum
target = 0
arr = [-1,0,1,2,-1,-4]
# arr = sorted(arr)
brr = set()
crr = []


for i in arr:
    for j in arr:
        for k in arr:
            if (i + j + k) == target:
                    # and (i != j and i != k and j != k)):
                brr.add(i)
                brr.add(j)
                brr.add(k)

                crr.append(list(brr) )


print(brr)


# A
n = input()
arr = list(map(int, n))
# print(arr)
large = sorted(arr)
small = sorted(arr, reverse=True)
# print(large)
# print(small)
lint = ""
for i in large:
    lint += str(i)
lint = int(lint)
# print(lint)
sint = ""
for i in small:
    sint += str(i)
sint = int(sint)
# print(sint)
print(abs(lint - sint))

# letbnbnb's go bois
