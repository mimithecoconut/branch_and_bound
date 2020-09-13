import csv 
import timeit 
import math

# finds 3^-1 mod N using Euclidean Algorithm
def find_inverse(N):
    N_0 = N
    a = 0
    b = 1
    y = 3
    if (N == 1):
        return 0
    while (y > 1): 
        q = y // N
        t = N
        N = y % N
        y = t 
        t = a
        a = b - q * a
        b = t
    if (b < 0): 
        b = b + N_0 
    return b

# evaluates f_l(y)
def f_l(y, l): 
    N = (int) (math.pow(2, l))
    inverse = find_inverse(N)
    sum = 0
    factor = 1
    for m in range(l):
        sum += math.cos((2 * math.pi * y * factor)/ N)
        factor *= (2 * inverse)
        factor = factor % N
    return sum / l

# finds the maximum f_l(y) for odd y
def f_lmax(l):
    maximum = f_l(1, l)
    N = (int) (math.pow(2, l))
    if (l != 1):
        for y in range(3, N, 2): 
            current = f_l(y, l)
            if (current > maximum):
                maximum = current 
    return round(maximum, 7) 
    


if __name__ == "__main__":
    with open('submissionA.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for l in range(1, 21):
            start = timeit.default_timer()
            f = f_lmax(l)
            stop = timeit.default_timer()
            time = round(stop - start, 3)
            writer.writerow([l, f, time])
