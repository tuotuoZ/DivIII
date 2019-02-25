decimal = int(input("Please enter a number: "))
digit = 1
while True:
	if decimal // (2 ** digit) == 0:
		digit -= 1
		break
	digit += 1

result = ''
while digit > -1:
	digit_num = decimal // (2 ** digit)
	result = result + str(digit_num)
	decimal = decimal % (2 ** digit)
	digit -= 1

print(result)

