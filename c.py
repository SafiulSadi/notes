# # C
import math
q = int(input())
while q > 0:
    n, t = map(int, input().split())
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
        print(count)

    q -= 1



    #
