num = "3.1415926535"
clear_num = ''
# for i in range(0, len(num)):
# 	if num[i] in '0123456789':
# 		clear_num = clear_num + num[i]
# 		print(clear_num)
#
# for i in range(0, 101, 5):
# 	print(i)

# Modify this loop to stop when i is exactly divisible by 11
for i in range(0, 100, 7):
	if (i % 11) == 0 and i != 0:
		break
	print(i)