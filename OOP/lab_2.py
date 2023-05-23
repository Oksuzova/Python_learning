# Oksuzova T. io-z21
import random


class First:
    def __init__(self):
        self.nzk = 2108
        self.c5 = self.nzk % 5      # 3 => C=A^B
        self.c7 = self.nzk % 7      # 1 => byte (int -128 to 127)
        self.c11 = self.nzk % 11    # 7 => Calculate the sum of the largest elements in the columns of the matrix
                                    # with odd numbers and the smallest elements in the columns
                                    # of the matrix with even numbers

    # method for creating matrix using random numbers in range from -128 to 127
    def matrix(self):
        row, col = 3, 3
        matrix1 = [[random.randrange(-128, 127) for y in range(col)] for x in range(row)]
        return matrix1

    # def m1_xor_m2(self, m1, m2):
    #     row = []
    #     matrix = []
    #     for i, j in zip(m1, m2):
    #         for k in range(len(i)):
    #             row.append(i[k] ^ j[k])
    #         matrix.append(row)
    #         row = []
    #     return matrix

    # def m1_xor_m2(self, m1, m2):
    #     row = []
    #     matrix = []
    #     for i in range(len(m1)):
    #         for j in range(len(m1[0])):
    #             row.append(m1[i][j] ^ m2[i][j])
    #         matrix.append(row)
    #         row = []
    #     return matrix

    # make list comprehension
    # def m1_xor_m2(self, m1, m2):
    #     row = []
    #     matrix = []
    #     for i, j in zip(m1, m2):
    #         for k, l in zip(i, j):
    #             row.append(k ^ l)
    #         matrix.append(row)
    #         row = []
    #     return matrix

    def m1_xor_m2(self, m1, m2):
        return [[k ^ l for k, l in zip(i, j)] for i, j in zip(m1, m2)]

    def result(self, m3):
        tmp = 127
        arr = []
        result = 0
        for item in range(len(m3)):
            self.column = [row[item] for row in m3]
            arr.append(self.column)
        for index, row in enumerate(arr):
            if index % 2 == 0:
                for item in row:
                    if item < tmp:
                        tmp = item
                if row.count(tmp) == 1:
                    result += tmp
                tmp = 0
            else:
                for item in row:
                    if item > tmp:
                        tmp = item
                if row.count(tmp) == 1:
                    result += tmp
                tmp = 127
        return result

    def display_matrix(self, m):
        for row in m:
            print(row)

def main():
    first = First()

    m1 = first.matrix()
    m2 = first.matrix()
    m3 = first.m1_xor_m2(m1, m2)

    print("The matrix A: ")
    first.display_matrix(m1)

    print("The matrix B: ")
    first.display_matrix(m2)

    print("The matrix of result A^B: ")
    first.display_matrix(m3)

    result = first.result(m3)
    print(f"Result of calculation: {result}")

if __name__ == '__main__':
    main()
