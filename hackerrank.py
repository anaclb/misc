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

def Median(arr):
    arr.sort()
    return arr[(int((len(arr)-1)/2))]
