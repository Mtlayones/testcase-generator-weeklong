from random import randrange, randint
num_testcase = 20
max_case = 10000
sub_case = max_case//num_testcase
max_traps = 100000000
sub_traps = max_traps//num_testcase
max_radius = 1000
max_points = 1000
filename = "testcase/input"
for i in range(num_testcase):
    case_i = randint(sub_case*i, sub_case*(i+1))
    with open(filename+str(i)+".txt", 'w') as writer:
        writer.write(str(case_i)+'\n')
        for j in range(case_i):
            num_traps = randint(sub_traps*i, sub_traps*(i+1))
            num_radius = randint(1, max_radius)
            q1 = randint(1, 4)
            if q1 == 1:
                data = [4, 2]
            elif q1 == 2:
                data = [1, 3]
            elif q1 == 3:
                data = [2, 4]
            else:
                data = [1, 3]
            q2 = data[randint(0, 1)]
            writer.write("{} {} {} {}\n".format(num_traps, num_radius, q1, q2))
            for k in range(num_traps):
                y1 = randint(-max_points, max_points)
                y2 = randint(-max_points, max_points)
                writer.write("{} {}\n".format(y1, y2))
