from random import randint
num_testcase = 20
max_length_arr = 100
sub_case = max_length_arr//20
max_number = 10000
filename = "testcase/input/input"
for i in range(num_testcase):
    with open(filename+str(i)+".txt", 'w') as writer:
        lenght_i = randint((sub_case*i)+1, sub_case*(i+1))
        writer.write(str(lenght_i)+'\n')
        string1 = ""
        string2 = ""
        for k in range(lenght_i-1):
            string1 += str(randint(1, max_number)) + ' '
            string2 += str(randint(1, max_number)) + ' '
        string1 += str(randint(1, max_number)) + ' '
        string2 += str(randint(1, max_number)) + ' '
        writer.write(string1+'\n')
        writer.write(string2+'\n')
        weight_capacity = randint(1, max_number)
        writer.write(str(weight_capacity)+'\n')
