import math

def plusMinus(arr):
    print("{:.6f}".format(len(list(filter(lambda x : x > 0, arr)))/n))
    print("{:.6f}".format(len(list(filter(lambda x : x < 0, arr)))/n))
    print("{:.6f}".format(len(list(filter(lambda x : x == 0, arr)))/n))

def miniMaxSum(arr):
    arr.sort()
    print(sum(arr[:-1]), sum(arr[1:]))

def timeConversion(s):
    time = s.split(":")
    if time[-1].find("AM") != -1:
        if time[0] == "12":
            time[0] = "00"
    elif time[0] != "12":
        time[0] = str(int(time[0])+12)
    return ':'.join(time)[:-2]

def median(arr):
    arr.sort()
    return arr[(int((len(arr)-1)/2))]

def lonelyinteger(a):
    for element in a:
        if a.count(element) == 1:
            return element

def diagonalDifference(arr):
    r_diag, l_diag = 0, 0
    for i in range(n):
        r_diag += arr[i][i]
        l_diag += arr[n-1-i][i]
    return abs(r_diag - l_diag)

def countingSort(arr):
    counter = [0] * 100
    for i in range(n):
        counter[arr[i]] += 1
    return counter

def flippingMatrix(matrix):
    n = len(matrix)
    print(n)
    soma = 0
    for i in range(n//2):
        for j in range(n//2):
            soma += max(matrix[i][j], matrix[i][n-j-1], matrix[n-i-1][j], matrix[n-i-1][n-j-1])
    return soma
