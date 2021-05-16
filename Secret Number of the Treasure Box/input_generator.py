from random import randrange, randint
num_testcase = 20
max_case = 1000
sub_case = max_case//num_testcase
max_length = 5000
max_number = 10000
filename = "testcase/input/input"
for i in range(num_testcase):
    case_i = randint(sub_case*i, sub_case*(i+1))
    with open(filename+str(i)+".txt", 'w') as writer:
        writer.write(str(case_i)+'\n')
        for j in range(case_i):
            lenght_i = randint(1, max_length)
            string1 = ""
            for k in range(lenght_i):
                string1 += str(randint(1, max_number)) + " "
            string1 = string1[:-1]
            writer.write(str(lenght_i)+'\n')
            writer.write(string1+'\n')
