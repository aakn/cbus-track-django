def convert(old):
	old = old.split('.')
	second = old.pop()

	deg_minute = old.pop()

	degree = float(deg_minute[:-2])
	minute = float(deg_minute[-2:])

	direction = second[-1:]

	second = "."+second[:-1]
	second = float(second)
	second = second * 60

	decimal = DMStoDEC(degree, minute, second)

	if direction == 'N' or direction == 'W':
		decimal *= -1


	return decimal

def DMStoDEC(degree, minute, second):
	return degree + ( ((minute*60) + (second)) /3600)