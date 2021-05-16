filename_o = "testcase/output/output"
filename_i = "testcase/input/input"
num_testcase = 20


def solve_gemstone_wheelbarrow(weights, worth, capacity):
    return gemstone_wheelbarrow(weights, worth, capacity, 0)


def gemstone_wheelbarrow(weights, worth, capacity, currentIndex):
    if capacity <= 0 or currentIndex >= len(worth):
        return 0

    worth1 = 0
    if weights[currentIndex] <= capacity:
        worth1 = worth[currentIndex] + gemstone_wheelbarrow(
            weights, worth, capacity - weights[currentIndex], currentIndex + 1)
    worth2 = gemstone_wheelbarrow(weights, worth, capacity, currentIndex + 1)
    return max(worth1, worth2)


for i in range(num_testcase):
    with open(filename_i + str(i) + ".txt", "r") as reader:
        with open(filename_o + str(i) + ".txt", "w") as writer:
            length = int(reader.readline())
            array1 = list(map(int, reader.readline()[:-1].split()))
            array2 = list(map(int, reader.readline()[:-1].split()))
            capacity = int(reader.readline())
            writer.write(str(solve_gemstone_wheelbarrow(
                array1, array2, capacity))+"\n")
