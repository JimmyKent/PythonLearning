import numpy as np


def read_data(filename, split):
    """
    读取文件,并作为矩阵输出
    filename:文件名
    split:分割标志
    """
    line_length = len(open(filename).readline().split(split))
    matrix_x = []

    file = open(filename)
    for line in file.readlines():
        line_arr = []
        cur_line = line.strip().split(split)
        for i in range(line_length):
            line_arr.append(float(cur_line[i]))
        matrix_x.append(line_arr)
    file.close()
    return np.mat(matrix_x)


def read_utf8(filename):
    file = open(filename, "r", encoding="utf-8")
    file.close()
    return file


def write_file_by_line(filename, data_list):
    file = open(filename, "w")
    for i in range(len(data_list)):
        file.write(data_list[i])
        file.write("\n")
    file.close()
    return


data = []
for i in range(10):
    data.append(str(i) )

write_file_by_line("test.txt", data)
