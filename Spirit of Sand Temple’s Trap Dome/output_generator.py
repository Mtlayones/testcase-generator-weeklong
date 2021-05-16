def radius_counter(x, y, radius):  # 6
    radius_temp = x**2 + y**2  # 4
    radius = radius ** 2  # 2
    return radius_temp < radius  # 1


def quadrant_detector(q1, q2, p1, p2):  # 28
    if q1 == 1 or q2 == 1:  # 7
        return True if p1 > 0 and p2 > 0 else False
    elif q1 == 2 or q2 == 2:
        return True if p1 < 0 and p2 > 0 else False
    elif q1 == 3 or q2 == 3:
        return True if p1 < 0 and p2 < 0 else False
    else:
        return True if p1 > 0 and p2 < 0 else False


filename_o = "testcase/output"
filename_i = "testcase/input"
num_testcase = 20
for i in range(num_testcase):
    with open(filename_i + str(i) + ".txt", "r") as reader:
        with open(filename_o + str(i) + ".txt", "w") as writer:
            test = int(reader.readline())
            for i in range(test):
                t, l, q1, q2 = [int(x) for x in reader.readline()[:-1].split()]
                counter = 0
                for traps in range(t):  # 240
                    y1, y2 = [int(x) for x in reader.readline()[:-1].split()]
                    if not quadrant_detector(q1, q2, y1, y2):  # 30
                        continue
                    if radius_counter(y1, y2, l):  # 8
                        counter += 1
                writer.write(str(counter)+"\n")
