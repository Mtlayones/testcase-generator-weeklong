from os import supports_bytes_environ


filename_o = "testcase/output/output"
filename_i = "testcase/input/input"
num_testcase = 20


def subsum(element, sum, N):
    dp = [[True for i in range(sum+1)] for j in range(N+1)]
    for s in range(1, sum+1):
        dp[0][s] = False
    for n in range(1, N+1):
        for s in range(1, sum+1):
            if element[n-1] <= s:
                dp[n][s] = dp[n-1][s] or dp[n-1][s-element[n-1]]
            else:
                dp[n][s] = dp[n-1][s]
    return dp[N][sum]


def equalsum(element, n):
    total = sum(element)
    if total % 2 == 0 and subsum(element, total//2, n):
        return True
    else:
        return False


for i in range(num_testcase):
    with open(filename_i + str(i) + ".txt", "r") as reader:
        with open(filename_o + str(i) + ".txt", "w") as writer:
            tcase = int(reader.readline())
            for i in range(tcase):
                length = int(reader.readline())
                arr = list(map(ord, list(reader.readline()[:-1])))
                if equalsum(arr, length):
                    writer.write("Hooman, take this loot\n")
                else:
                    writer.write(
                        "Hooman, you will suffer an endless punishment\n")
