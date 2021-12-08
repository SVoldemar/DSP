import numpy as np

if __name__ == '__main__':
    size = 11  # size of array
    arr = np.zeros([size, size])  # zero filling array
    print(arr)  # output array values
    print("################################################")
    for i in range(size):  # changing values of array
        for j in range(size):
            if i == j:
                arr[i][j] = 1
            elif size - i - 1 == j:
                arr[i][j] = 1

    print(arr)  # output array values


