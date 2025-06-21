import numpy as np

test_1 = np.array([92, 94, 88, 91, 87])
test_2 = np.genfromtxt('test_2.csv', delimiter=',')

# array operations 
test_3 = np.array([87, 85, 72, 90, 92])
test_3_fixed = test_3 + 2

# multiple numpy array ops
total_grade = test_1 + test_2 + test_3_fixed
final_grade = total_grade / 3
print(final_grade)

# multi-dimensional arrays
coin_toss = np.array([1, 0, 0, 1, 0])

coin_toss_again = np.array([[1, 0, 0, 1, 0], [0, 0, 1, 1, 1]])