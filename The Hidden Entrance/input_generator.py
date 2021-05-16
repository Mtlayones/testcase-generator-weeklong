from random import randrange, randint
num_testcase = 20
characters = ["\\", "/"]
max_case = 100000
sub_case = max_case//num_testcase
max_length = 1000
filename = "testcase/input"
for i in range(num_testcase):
    case_i = randint(sub_case*i, sub_case*(i+1))
    with open(filename+str(i)+".txt", 'w') as writer:
        writer.write(str(case_i)+'\n')
        for j in range(case_i):
            lenght_i = randrange(1, max_length, 2)
            string1 = ""
            for k in range((lenght_i-1)//2):
                string1 += characters[randint(1, 1000) % 2] + 'O'
            string1 += characters[randint(1, 1000) % 2]
            writer.write(str(lenght_i)+'\n')
            writer.write(string1+'\n')
