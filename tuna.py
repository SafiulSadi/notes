# # C
import math
q = int(input())
while q > 0:
    n, t = map(int, input().split())
    # srr = set()
    if t == 1:
        print(n)
    else:
        t -= 1
        count = 0
        for i in range(1, int(t ** 0.5) + 1):
            if t % i == 0:
                # srr.add(i)
                if i < n:
                    count += 1
                if t // i <= n and t //i != i:
                    count += 1
                pass
        # crr = set()

        # for i in srr:
        #     if i != t // i:
        #         if i <= t:
        #             crr.add(t // i)

        # for i in range(1, int((n+1))):
        #     if t % i == 1:
        #         count += 1


        print(count)
    #
#
# #
# def count_divisors_leq_n(D, N):
#     count = 0
#     for i in range(1, int(D**0.5) + 1):
#         if D % i == 0:
#             if i <= N:
#                 count += 1
#             if D // i <= N and D // i != i:
#                 count += 1
#     return count
#
# def count_cuckoo_clocks(Q, test_cases):
#     results = []
#     for case in test_cases:
#         N, T = case
#         if T == 1:
#             results.append(1)
#         else:
#             D = T - 1
#             results.append(count_divisors_leq_n(D, N))
#     return results
#
# # Reading input
# Q = int(input())
# test_cases = [tuple(map(int, input().split())) for _ in range(Q)]
#
# # Getting the results
# results = count_cuckoo_clocks(Q, test_cases)
#
# # Printing the results
# for result in results:
#     print(result)

# def count_divisors_leq_n(D, N):
#     count = 0
#     for i in range(1, min(N, D) + 1):
#         if D % i == 0:
#             count += 1
#     return count
#
# def count_cuckoo_clocks(Q, test_cases):
#     results = []
#     for case in test_cases:
#         N, T = case
#         if T == 1:
#             results.append(1)
#         else:
#             D = T - 1
#             results.append(count_divisors_leq_n(D, N))
#     return results
#
# # Reading input
# Q = int(input())
# test_cases = [tuple(map(int, input().split())) for _ in range(Q)]
#
# # Getting the results
# results = count_cuckoo_clocks(Q, test_cases)
#
# # Printing the results
# for result in results:
#     print(result)