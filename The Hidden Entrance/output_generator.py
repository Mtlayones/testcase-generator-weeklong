filename_o = "testcase/output"
filename_i = "testcase/input"
num_testcase = 20


for i in range(num_testcase):
    with open(filename_i + str(i) + ".txt", "r") as reader:
        with open(filename_o + str(i) + ".txt", "w") as writer:
            test = int(reader.readline())
            for i in range(test):
                length = int(reader.readline())
                input1 = reader.readline()[:-1]
                if(input1[-1] == "/"):
                    writer.write("HOORAY HOOMAN!"+"\n")
                else:
                    writer.write("YOU ARE DOOMED!"+"\n")
