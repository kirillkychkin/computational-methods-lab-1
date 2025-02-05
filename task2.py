import matplotlib.pyplot as plt

pi_arr = [
    3.14159265358979,
    3.141592653589,
    3.1415926535,
    3.14159265,
    3.141592,
    3.1415,
    3.14,
    3
]
abs_err = list()
rel_err = list()
n = 0
while n < len(pi_arr):
    # print("parameter " + str(n + 1))
    # up_method
    res1 = 0
    for i in range(1, 1000001):
        res1 += pi_arr[n] / (i * i)
    # print(res1)

    # low_method
    res2 = 0
    for i in range(1000000, 0, -1):
        res2 += pi_arr[n] / (i * i)
    # print(res2)

    diff = abs(res2 - res1)
    abs_err.append(diff)
    # print("absolute error:" + str(diff))

    diff = abs(res1 - res2) / res1
    # print("relative error:" + str(diff))
    rel_err.append(diff)
    n+=1
    print("==========")
plt.plot(abs_err)
plt.show()