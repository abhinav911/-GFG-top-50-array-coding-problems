# User function Template for python3


def getMinMax(a, n):
    min = a[0]
    max = a[n - 1]
    for i in range(n):
        if (a[i] <= min):
            min = a[i]
        if (a[i] >= max):
            max = a[i]
    return min, max


