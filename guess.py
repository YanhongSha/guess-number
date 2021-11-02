# guess number
import random
x = input('Please define the random upper limit:')
x = int(x)
r = random.randint(1,x)
count = 0
while True:
	count = count + 1
	x = input('please input a number:')
	x = int(x)
	if x == r:
		print('congratulaitons! you take', count, 'to get the result')
		break
	elif x > r:
		print('it is too big,try again! This is', count, 'times')
	elif x < r:
		print('it is too small, try again! This is', count, 'times')

