import numpy as np
import statistics
import random

# Question 1
print('Question 1')
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = a + b
print(c)

# Question 2
print('Question 2')
zeros1 = np.array([0,0,0,0,0,0,0,0,0,0])

print(zeros1.shape)
print()
zeros2 = zeros1.reshape(2, 5)
print(zeros2)

# Question 3
print('Question 3')
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
data = np.array(data)

mean = data.mean()
median = statistics.median(data)
mode = statistics.mode(data)
s_deviation = statistics.stdev(data)

print(mean)
print()
print(median)
print()
print(mode)
print()
print(s_deviation)
print()

# Question 4
print('Question 4')
rand_numbers = random.sample(range(1,100), 36)
rand_array = np.array(rand_numbers)
rand_array = rand_array.reshape(6, 6)
print(rand_array.min())
print()
print(rand_array.max())

# Question 5
print('Question 5')
array_3d = np.array([[[13, 9], [16, 23]],[[12, 21], [10, 99]], [[36, 57],[65, 12]]])

array_2d = np.reshape(array_3d, (4, 3))

print(array_2d)

# Question 6
print('Question 6')
data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

data_1d = np.reshape(data, (9))

print(data_1d)