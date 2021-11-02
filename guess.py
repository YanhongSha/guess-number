# guess number
import random
r = random.randint(1,50)

while True:
	x = input('please input a number:')
	x = int(x)
	if x == r:
		print('congratulaitons!')
		break
	elif x > r:
		print('it is too big,try again!')
	elif x < r:
		print('it is too small, try again!')
