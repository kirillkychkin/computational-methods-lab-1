import math

#up_method
res1 = 0
for i in range(1, 1000001):
    res1 += math.pi / (i * i)
print(res1)

#low_method
res2 = 0
for i in range(1000000, 0, -1):
    res2 += math.pi / (i * i)
print(res2)

diff = abs(res2 - res1)
print("absolute error:" + str(diff))

diff = abs(res1 - res2) / res1
print("relative error:" + str(diff))