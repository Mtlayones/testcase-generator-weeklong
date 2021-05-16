import math
from os import TMP_MAX

filename_o = "testcase/output/output"
filename_i = "testcase/input/input"
num_testcase = 20


def max_gcd(arr, n):
    max_gcd = 0
    for i in range(1, n):
        temp = math.gcd(arr[i], arr[i-1])
        if temp > max_gcd:
            max_gcd = temp
    return max_gcd


for i in range(num_testcase):
    with open(filename_i + str(i) + ".txt", "r") as reader:
        with open(filename_o + str(i) + ".txt", "w") as writer:
            test = int(reader.readline())
            for i in range(test):
                length = int(reader.readline())
                input1 = list(map(int, reader.readline()[:-1].split()))
                writer.write(str(max_gcd(input1, length))+"\n")
