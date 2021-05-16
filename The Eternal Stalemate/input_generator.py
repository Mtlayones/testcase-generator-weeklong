from random import randrange, randint
num_testcase = 20
max_size = 20
filename = "testcase/input/input"
for i in range(num_testcase):
    with open(filename+str(i)+".txt", 'w') as writer:
        matrix_size = randint(1, max_size)
        writer.write(str(matrix_size)+'\n')
        for j in range(matrix_size):
            series_num = "0 "*matrix_size
            series_num = series_num[:-1]
            writer.write(series_num+'\n')
