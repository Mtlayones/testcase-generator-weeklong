from random import randint
num_testcase = 20
max_case = 100
sub_case = max_case//20
max_length = 100
filename = "testcase/input/input"
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
for i in range(num_testcase):
    case_i = randint(sub_case*i, sub_case*(i+1))
    with open(filename+str(i)+".txt", 'w') as writer:
        writer.write(str(case_i)+'\n')
        for j in range(case_i):
            lenght_i = randint(1, max_length)
            string1 = ""
            for k in range(lenght_i):
                string1 += characters[randint(1, 1000) % 62]
            writer.write(str(lenght_i)+'\n')
            writer.write(string1+'\n')
