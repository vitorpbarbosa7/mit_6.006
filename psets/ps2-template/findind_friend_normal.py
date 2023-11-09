


a = 0
n = 100
card = 99

k = 50
left = a
right = n

while k != card:
	if card > k:
		print('north')
		left = k
		k = (left + right)//2
		print(f'new k: {k} \n')
	else:
		print('south')
		right = k
		k = (left + right)//2
		print(f'new k: {k} \n')


