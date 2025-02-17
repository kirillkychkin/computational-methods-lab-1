import matplotlib.pyplot as plt
import math

# accurate
accurate = 0
for i in range(1000000, 0, -1):
    accurate += math.pi / (i * i)
# print(res2)
# accurate = 5.167709638458887

# accurate low
accurate_low = 0
for i in range(1, 1000001):
    accurate_low += math.pi / (i * i)


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
abs_err_up = list()
rel_err_up = list()
abs_err_low = list()
rel_err_low = list()
method_abs_err = list()
method_rel_err = list()
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

    diff = abs(accurate - res1)
    abs_err_up.append(diff)

    diff = abs(accurate - res2)
    abs_err_low.append(diff)

    diff = abs(accurate_low - res1)
    method_abs_err.append(diff)

    diff = abs(res1 - accurate) / res1
    rel_err_up.append(diff)

    diff = abs(res2 - accurate) / res2
    rel_err_low.append(diff)

    diff = abs(res2 - accurate_low) / res2
    method_rel_err.append(diff)

    n+=1
    # print("==========")
# print(abs_err_up)
# print(rel_err_up)
pi_log_arr = list()
for i in pi_arr:
    pi_log_arr.append(math.log(i, 10))

'''
1 график - методология + округление
2 график - округление
3 график - разницы (округление минус метод + округление)
4 график - сравнить точное значение минус округ + метод И  массив округления неточное значение (math_pi 1 - 10^6) с округ + метод
'''
# методология + округления - округление = методология
subtract_abs_arr = list()
subtract_rel_arr = list()
for i in range(len(abs_err_low)):
    subtract_abs_arr.append(abs_err_up[i] - abs_err_low[i])
    subtract_rel_arr.append(rel_err_up[i] - rel_err_low[i])
    
# округление (точное ) минус округление (не точное)
round_list_abs = list()
round_list_rel = list()
for i in range(len(abs_err_low)):
    round_list_abs.append(abs_err_low[i] - method_abs_err[i])
    round_list_rel.append(rel_err_low[i] - method_rel_err[i])

abs_err_up = [math.log(e) for e in abs_err_up]
rel_err_up = [math.log(e) for e in rel_err_up]
fig, ax = plt.subplots(4)
ax[0].set_xlabel('pi') 
ax[0].set_ylabel('log error')
ax[0].plot(range(1,9), abs_err_up, label='absolute', marker='.', linestyle='-')
ax[0].plot(range(1,9), rel_err_up, label='relative', marker='.', linestyle='-')
ax[0].set_title("мет. ошибка и ошибка округления")
ax[0].legend()

abs_err_low = [math.log(e) for e in abs_err_low]
rel_err_low = [math.log(e) for e in rel_err_low]
ax[1].set_xlabel('pi') 
ax[1].set_ylabel('log error')
ax[1].plot(range(1,9), abs_err_low, label='absolute', marker='.', linestyle='-')
ax[1].plot(range(1,9), rel_err_low, label='relative', marker='.', linestyle='-')
ax[1].set_title("ошибка округления")
ax[1].legend()

ax[2].set_xlabel('pi') 
ax[2].set_ylabel('log error')
ax[2].plot(range(1,9), subtract_abs_arr, label='absolute', marker='.', linestyle='-')
ax[2].plot(range(1,9), subtract_rel_arr, label='relative', marker='.', linestyle='-')
ax[2].set_title("методология + округления - округление = методология")
ax[2].legend()

ax[3].set_xlabel('pi') 
ax[3].set_ylabel('log error')
ax[3].plot(range(1,9), round_list_abs, label='absolute', marker='.', linestyle='-')
ax[3].plot(range(1,9), round_list_rel, label='relative', marker='.', linestyle='-')
ax[3].set_title("округление (точное ) минус округление (не точное)")
ax[3].legend()



plt.show()