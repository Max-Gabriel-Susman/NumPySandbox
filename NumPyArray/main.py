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

# selecting elements from single dimensional arrays by index
jeremy_test_2 = test_2[3]
manual_adwoa_test_1 = np.array([test_1[1], test_1[2]])

# multi-dimensional arrays
coin_toss = np.array([1, 0, 0, 1, 0])

coin_toss_again = np.array([[1, 0, 0, 1, 0], [0, 0, 1, 1, 1]])

# selecting elements from multi-dimensional arrays 
student_scores = np.array([[92, 94, 88, 91, 87],
                           [79, 100, 86, 93, 91],
                           [87, 85, 72, 90, 92]])

tanya_test_3 = student_scores[2, 0]

cody_test_scores = student_scores[:,4]

# logical operations with arrays
porridge = np.array([79, 65, 50, 63, 56, 90, 85, 98, 79, 51])

cold = porridge[porridge < 60]
hot = porridge[porridge > 80]
just_right = porridge[(porridge >= 60) & (porridge <= 80)]
print(cold)
print(hot)
print(just_right)