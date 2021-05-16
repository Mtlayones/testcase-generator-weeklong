from os import supports_bytes_environ
import sys

filename_o = "testcase/output/output"
filename_i = "testcase/input/input"
num_testcase = 20


def mindiffsubsum(element, N):
    all = sum(element)
    dp = [[True for i in range(all + 1)] for j in range(N+1)]

    for s in range(1, all + 1):
        dp[0][s] = False

    for n in range(1, N+1):
        for s in range(1, all + 1):
            if element[n-1] <= s:
                dp[n][s] = dp[n-1][s] or dp[n-1][s-element[n-1]]
            else:
                dp[n][s] = dp[n-1][s]
    min = sys.maxsize
    for i in range(0, all + 1):
        if dp[N][i] and min > abs(all-2*i):
            min = abs(all - 2 * i)

    return min


for i in range(num_testcase):
    with open(filename_i + str(i) + ".txt", "r") as reader:
        with open(filename_o + str(i) + ".txt", "w") as writer:
            tcase = int(reader.readline())
            for i in range(tcase):
                length = int(reader.readline())
                arr = list(map(ord, list(reader.readline()[:-1])))
                writer.write(str(mindiffsubsum(arr, length))+"\n")
